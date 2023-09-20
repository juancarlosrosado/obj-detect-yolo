import os
from dotenv import load_dotenv
import datetime
import json
import cv2
from ultralytics import YOLO
import fastapi
import uvicorn

load_dotenv()

if not os.path.exists("predictions"):
    os.makedirs("predictions")

app = fastapi.FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/predict/{photo_path}/{file_id}")
def predict(photo_path, file_id):
    """
    Realiza una predicción sobre una imagen
    """
    try:
        WEIGHTS_PATH = os.getenv("WEIGHTS_PATH")

        source = cv2.imread(photo_path)
        datetime_cet = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        model = YOLO(WEIGHTS_PATH)
        results = model.predict(
            source=source,
            save=True,
            project="predictions",
            name=file_id,
            exist_ok=True,
        )

        for result in results:
            detection_count = result.boxes.shape[0]

            my_dict = []

            for i in range(detection_count):
                cls = int(result.boxes.cls[i].item())
                name = result.names[cls]
                confidence = float(result.boxes.conf[i].item())
                obj = {
                    "id": file_id,
                    "datetime": datetime_cet,
                    "name": name,
                    "probability": round(confidence, 4),
                }
                my_dict.append(obj)

            with open(f'predictions/{file_id}/{obj["id"]}.json', "a") as json_file:
                json.dump(my_dict, json_file, indent=4)

        return print("Done")

    except Exception as e:
        raise fastapi.HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
