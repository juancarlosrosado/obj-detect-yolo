import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import uvicorn

from YOLO import predict_YOLO

load_dotenv()

if not os.path.exists("predictions"):
    os.makedirs("predictions")

app = FastAPI(tittle="YOLO API")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict/")
def predict(photo_path, file_id):
    modelYOLO = predict_YOLO(photo_path, file_id)

    if not modelYOLO:
        # the exception is raised, not returned - you will get a validation error otherwise

        raise HTTPException(status_code=404, detail="Image could not be downloaded")

    return {
        "status_code": 200,
        "ingredient": modelYOLO["ingredient"],
        "probability": modelYOLO["probability"],
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
