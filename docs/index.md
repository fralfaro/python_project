# Welcome to Data Science Project Docs!

<img src="https://images.viblo.asia/35852bff-d14e-457f-b562-00db7c0494cb.png" width="500" >


Structuring your data science project according to established standards is paramount to ensure seamless collaboration 
and facilitate the maintenance and modification of your work by team members.

This repository offers a comprehensive example crafted to embrace industry best practices, 
aimed at enabling the creation of a data science project that is not only robust but also highly reproducible.

## About repository structure

```
├───data
│   ├───input
│   │   ├───datos_a_trabajar.csv
│   │   ├───datos_a_trabajar.gzip
│   │   └─── ...
│   └───output
│       ├───models_metrics.csv
│       └───uplift.csv
├───ds_project
│   ├───notebooks
│   │   ├───eda.ipynb
│   │   ├───metrics.ipynb
│   │   └───models.ipynb
│   ├───metrics.py
│   ├───models.py
│   └───utils.py
├───images
│   └───metrics
│       ├───curva_roc.png
│       ├───feature_importance.png
│       └───uplift.png
├───models
│   └───model.pkl
├───.gitignore
├───poetry.lock
├───poetry.toml
└────README.md
```

Where:

- **data**: Almacena datos utilizados en el proyecto. Suele estar dividido en subcarpetas:
  - **input**: Contiene datos de entrada, como archivos CSV, bases de datos o cualquier información relevante que se utilice para el análisis o modelado.
  - **output**: Contiene los resultados generados durante el análisis o modelado, como archivos de resultados, métricas, o cualquier otro tipo de salida.

- **ds_project**: Directorio principal del proyecto.
  - **notebooks**: Contiene notebooks de Jupyter, que pueden incluir análisis exploratorio de datos, pruebas de modelos, visualizaciones, entre otros.
  - **metrics.py**: Un archivo de Python que puede contener funciones o clases para calcular métricas específicas utilizadas en el proyecto.
  - **models.py**: Archivo que puede contener definiciones de modelos de Machine Learning o funciones relacionadas con el entrenamiento y evaluación de modelos.
  - **utils.py**: Archivo que alberga funciones o utilidades compartidas en todo el proyecto.

- **images**: Almacena imágenes o gráficos generados durante el análisis de datos, visualizaciones o resultados de modelos.
  - **metrics**: Carpeta específica para imágenes relacionadas con las métricas o evaluación de modelos.

- **models**: Contiene modelos entrenados guardados en archivos, como archivos de modelo serializados (por ejemplo, pickle, joblib) o archivos guardados en formatos específicos para modelos de Machine Learning.
- **.gitignore**: Archivo que enumera los archivos y carpetas que se deben ignorar en el control de versiones mediante Git.
- **poetry.lock**: Archivo generado por la herramienta de manejo de dependencias Poetry, que detalla las versiones específicas de las dependencias del proyecto.
- **poetry.toml**: Archivo de configuración de Poetry que contiene información sobre el proyecto y sus dependencias.
- **README.md**: Archivo de documentación que proporciona información general sobre el proyecto, su estructura y cómo ejecutarlo.


## Tools used in this project

In this project, we've utilized a variety of 
powerful tools and libraries to enhance our data 
science workflow and maintain code quality. 

Here are some similar examples for the
packages you've mentioned, along with relevant
articles or documentation:

1. **Poetry (Dependency Management):**
     - Poetry is used to manage project dependencies efficiently.
     - Documentation: [Poetry Documentation](https://python-poetry.org/)

2. **Pydantic (Data Validation and Parsing):**
     - Pydantic is employed for data validation and parsing.
     - Documentation: [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

3. **Mkdocs (Documentation Generation):**
     - Mkdocs is employed to generate project documentation.
     - Documentation: [Mkdocs Documentation](https://www.mkdocs.org/)

4. **Pandas (Data Manipulation):**
     - Pandas is used for data manipulation and analysis.
     - Documentation: [Pandas Documentation](https://pandas.pydata.org/docs/)

5. **Scikit-Learn (Machine Learning):**
     - Scikit-Learn is utilized for machine learning tasks.
     - Documentation: [Scikit-Learn Documentation](https://scikit-learn.org/stable/documentation.html)

6. **Pre-commit (Code Review and Formatting):**
     - Pre-commit helps automate code review and formatting tasks.
     - Documentation: [Pre-commit Documentation](https://pre-commit.com/)

7. **Black (Code Formatting):**
     - Black is employed for code formatting to ensure consistency.
     - Documentation: [Black Documentation](https://black.readthedocs.io/en/stable/)

8. **Flake8 (Code Linting):**
     - Flake8 is used for code linting to catch potential issues.
     - Documentation: [Flake8 Documentation](https://flake8.pycqa.org/en/latest/)

9. **Pytest (Testing):**
     - Pytest is used for writing and running tests.
     - Documentation: [Pytest Documentation](https://docs.pytest.org/en/latest/)

