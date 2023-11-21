# Reporte de Desarrollo y Despliegue de la API FastAPI y la Aplicación React

## Descripción General

Este proyecto consta de una API desarrollada con FastAPI y una aplicación cliente desarrollada con React. La API está diseñada para detectar armas en imágenes utilizando un modelo de visión artificial. La aplicación React permite a los usuarios interactuar con la API, subiendo imágenes para su análisis, verificando el estado del servicio y descargando reportes de predicciones.

### Características de la API FastAPI

- *Detección de Armas:* Analiza imágenes subidas para detectar la presencia de armas.
- *Reporte de Estado:* Proporciona información sobre el estado actual del servicio.
- *Generación de Reportes:* Crea un reporte en formato CSV con el historial de predicciones.

### Características de la Aplicación React

- *Interfaz de Usuario:* Permite a los usuarios cargar imágenes para análisis.
- *Visualización de Resultados:* Muestra si se han detectado armas en las imágenes cargadas.
- *Descarga de Reportes:* Facilita la descarga de reportes generados por la API.

## Requerimientos y Configuración

### Para la API FastAPI

- *Python:* Versión 3.7 o superior.
- *Bibliotecas de Python:* FastAPI, Uvicorn (como servidor), Pillow, NumPy, y cualquier otra dependencia requerida por `predictor`.
- *Modelo de Visión Artificial:* El modelo debe estar correctamente configurado y accesible por la API.

#### Instalación de Dependencias

Instalar las dependencias con pip:

bash
pip install fastapi uvicorn python-multipart pillow numpy


#### Ejecución de la API

Ejecutar el archivo principal (por ejemplo, `main.py`) con Uvicorn:

bash
uvicorn main:app --reload


### Para la Aplicación React

- *Node.js y npm:* Se requiere la última versión estable.
- *React:* Framework para el desarrollo de la interfaz de usuario.
- *Axios:* Para realizar solicitudes HTTP a la API.

#### Instalación de Dependencias

Crear un nuevo proyecto React y añadir Axios:

bash
npx create-react-app react-gun-detector
cd react-gun-detector
npm install axios


#### Ejecución de la Aplicación

Iniciar la aplicación en modo de desarrollo:

bash
npm start


## Problemas Encontrados y Soluciones

### Problema de CORS en la API

*Problema:* La aplicación React no podía conectarse a la API FastAPI debido a restricciones de CORS.

*Solución:* Se configuró el middleware CORS en FastAPI para permitir solicitudes desde el origen de la aplicación React.

### Formato de Respuesta de la API

*Problema:* La API devolvía datos crudos que no eran claros para el usuario final.

*Solución:* Se modificó la API y la aplicación React para interpretar los datos y mostrar mensajes amigables al usuario.

### Manejo de Archivos en React

*Problema:* Dificultades en el manejo y carga de archivos de imagen en la aplicación React.

*Solución:* Uso de `FormData` en React y configuración adecuada de los endpoints en FastAPI para manejar los archivos multimedia.

## Conclusión

Este conjunto de herramientas proporciona una solución completa y eficiente para la detección de armas en imágenes. La API FastAPI procesa las imágenes y genera reportes, mientras que la aplicación React ofrece una interfaz de usuario amigable para interactuar con la API, lo que resulta en un sistema integrado y fácil de usar.
