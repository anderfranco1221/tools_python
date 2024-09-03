
## Descripción

Este proyecto está desarrollado con **FastAPI** y tiene como funcionalidades principales la extracción de texto en imágenes utilizando la librería **Tesseract** y la generación de archivos Excel a partir de datos JSON. Además, el proyecto cuenta con una configuración de **GitHub Actions** que automatiza procesos basados en los commits realizados.

## Funcionalidades

- **Extracción de texto en Imágenes**: 
  - Se implementó el reconocimiento de texto en imágenes utilizando la librería **Tesseract**.
  - Este servicio permite extraer texto de imágenes enviadas a través de un endpoint específico.

- **Generación de Archivos Excel**:
  - Un endpoint recibe datos en formato JSON y genera un archivo Excel con la información proporcionada.
  - Esta funcionalidad es útil para la exportación y manejo de datos en un formato ampliamente utilizado.

- **Integración Continua con GitHub Actions**:
  - Se configuraron **GitHub Actions** para ejecutar tareas automatizadas, como pruebas, linting y despliegues según los commits.
  - Esto asegura que el código en la rama principal se mantenga en un estado óptimo.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

/project-root │ Se encuentra los instalables,  la creación de la imagen, el instalable .yml, los instalables en Windows.
├── /app │ Los archivos de configuracion de fast api
├── /Controllers# Endpoints de la API │
├── /negocio # Logica de los controladores │ 
├── /helpers # Utilidades como la generación de Excel │
├── main.py # Punto de entrada de la aplicación FastAPI 
├── requirements.txt # Dependencias del proyecto
└── .github/workflows # Configuraciones de GitHub Actions


