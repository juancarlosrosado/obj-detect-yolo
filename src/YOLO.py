import os
from dotenv import load_dotenv
import datetime
import json
import cv2
from ultralytics import YOLO

load_dotenv()


if not os.path.exists("predictions"):
    os.makedirs("predictions")


def predict_YOLO(photo_path, file_id):
    """
    Realiza una predicción sobre una imagen

    Output:
    - Imagen con las predicciones
    - Fichero JSON con las predicciones:
        {
            "id": id,
            "datetime": fecha y hora de la predicción,
            "ingredient": ingrediente,
            "probability": probabilidad de que sea ese ingrediente,
        }
    """
    try:
        if os.getenv("WEIGHTS_PATH") is None:
            raise Exception("WEIGHTS_PATH not found")

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
                    "ingredient": name,
                    "probability": round(confidence, 4),
                }
                my_dict.append(obj)

            with open(f'predictions/{file_id}/{obj["id"]}.json', "a") as json_file:
                json.dump(my_dict, json_file, indent=4)

        return json.dumps(my_dict)

    except Exception as e:
        print(e)
