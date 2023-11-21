import io
import csv
from datetime import datetime
import cv2
from fastapi import FastAPI, UploadFile, File, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import numpy as np
from predictor import GunsPredictor, PersonsPredictor  # Asegúrate de que este módulo esté correctamente implementado

app = FastAPI(title="Gun Detection API")

# Configuración de CORS para permitir solicitudes desde el frontend React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Cambia esto según tus necesidades
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Nombre del archivo de reporte
report_file = "predictions_report.csv"

# Inicialización del predictor
predictor = GunsPredictor()
persons_predictor = PersonsPredictor()

# Inicializa el archivo de reporte si no existe
def initialize_report_file():
    try:
        with open(report_file, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["File Name", "Date Time", "Number of Pistols Detected", "Number of Persons Detected", "Image with Detections"])
    except FileExistsError:
        pass

initialize_report_file()

@app.get("/status")
def get_status():
    return {"status": "Servicio en funcionamiento", "model_info": "Modelo de detección de armas"}

@app.post("/predict_gun")
async def predict_gun(file: UploadFile = File(...)):
    if file.content_type.split("/")[0] != "image":
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="Not an image")

    try:
        # Procesa la imagen y realiza la predicción
        img_stream = io.BytesIO(await file.read())
        img = Image.open(img_stream)
        img_array = np.array(img)
        num_pistols, boxes = predictor.predict_file(img_array)  # Asegúrate de que esta función acepte np.array
        num_personas, boxes_personas = persons_predictor.predict_file(img_array)

        # Dibuja las cajas delimitadoras en la imagen
        for box in boxes:
            start_point = (int(box[0]), int(box[1]))
            end_point = (int(box[2]), int(box[3]))
            color = (255, 0, 0)  # Color rojo
            thickness = 2
            img_array = cv2.rectangle(img_array, start_point, end_point, color, thickness)

        # Dibuja las cajas delimitadoras de personas en la imagen
        for box in boxes_personas:
            start_point = (int(box[0]), int(box[1]))
            end_point = (int(box[2]), int(box[3]))
            color = (0, 255, 0)  # Color verde
            thickness = 2
            img_array = cv2.rectangle(img_array, start_point, end_point, color, thickness)

        # Guarda la imagen con las cajas delimitadoras de personas y armas
        img_with_boxes_person = Image.fromarray(img_array)
        img_with_boxes_person.save(f"fastapi/images_upload/{file.filename.split('.')[0]}_with_boxes.jpg")  # Guarda la imagen en la carpeta fastapi

        # Registro de la predicción en el archivo CSV
        with open(report_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([file.filename, datetime.now().isoformat(), num_pistols, num_personas, f"/images_upload/{file.filename.split('.')[0]}_with_boxes.jpg"])
        
        return {"num_pistols": num_pistols, "num_persons": num_personas}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))

@app.get("/reports")
def get_reports():
    with open(report_file, "r", newline="") as f:
        return Response(content=f.read(), media_type="text/csv", headers={"Content-Disposition": "attachment; filename=predictions_report.csv"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)