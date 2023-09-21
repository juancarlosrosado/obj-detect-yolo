import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, UploadFile
import uvicorn

from YOLO import predict_YOLO

load_dotenv()

if not os.path.exists("predictions"):
    os.makedirs("predictions")

app = FastAPI(title="YOLO API")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict/")
async def predict(file: UploadFile):
    try:
        # Guarda el archivo cargado en el servidor
        file_id = file.filename
        with open(f"uploads/{file_id}", "wb") as f:
            f.write(file.file.read())

        # Realiza la predicción usando tu función predict_YOLO
        photo_path = f"uploads/{file_id}"
        modelYOLO = predict_YOLO(photo_path, file_id)

        if not modelYOLO:
            raise HTTPException(status_code=404, detail="No se pudo procesar la imagen")

        return {
            "status_code": 200,
            "ingredient": modelYOLO["ingredient"],
            "probability": modelYOLO["probability"],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
