### Informe del Proyecto

### Estudiantes
Samuel Matias Escobar Bejarano
56825
Ignacio Lizarazu Aramayo
47046

#### IMPORTANTE
Para el correcto funcionamiento es importante:
- MODIFICAR el archivo /fastapi/predictor en la linea 3 donde es necesario introducir el PATH absoluto de la carpeta donde se clono el repositorio
- En una terminal dirigirse hasta la carpeta /fastapi/ y ejecutar el comando uvicorn app:app -reload

#### 1. `app.py` (Aplicación FastAPI)
- *Funcionalidad*: Este archivo Python es la parte de backend de una aplicación web utilizando FastAPI. Incluye importaciones para el manejo de archivos, imágenes y solicitudes HTTP.
- *Características Clave*:
  - Manejo de archivos con CSV y procesamiento de imágenes con OpenCV y PIL.
  - Configuración de FastAPI con rutas para subir y procesar archivos.
  - Configuración de middleware CORS (Cross-Origin Resource Sharing), probablemente para permitir solicitudes desde el frontend.
  - Integración con un módulo llamado `predictor` (posiblemente `predictor.py`), que parece manejar tareas específicas de predicción relacionadas con armas y personas.

- *Requisitos*:
  - Entorno Python.
  - Biblioteca FastAPI.
  - Bibliotecas para manejo de archivos e imágenes (`io`, `csv`, `cv2`, `PIL`).
  - Configuración adecuada del módulo `predictor`.

#### 3. `predictor.py`
- *Funcionalidad*: No se pudo acceder al contenido directamente. Presumiblemente, contiene la lógica para hacer predicciones, posiblemente relacionadas con armas y personas, como se infiere de `app.py`.
- *Requisitos*:
  - Entorno Python.
  - Bibliotecas para procesamiento y predicción (potencialmente OpenCV, PIL, o similares).
  - Debe estar correctamente implementado e integrado con `app.py`.

#### Pasos para Ejecutar la Aplicación
1. *Configuración del Backend (FastAPI)*
   - Asegurarse de que Python y las bibliotecas requeridas estén instaladas.
   - Configurar `predictor.py` correctamente.
   - Modificar la línea 3 en `predictor.py` para especificar la ruta absoluta donde se clonó el repositorio.
   - Ejecutar `app.py` para iniciar el servidor FastAPI.

3. *Interacción*
   - El backend procesa los archivos y devuelve resultados, que se muestran en el frontend.

Sin acceso al contenido completo de los archivos, especialmente `predictor.py`, este resumen se basa en el contenido parcial disponible y suposiciones sobre estructuras típicas de tales aplicaciones. Para una descripción más detallada y precisa, es necesario tener acceso al contenido completo de todos los archivos.