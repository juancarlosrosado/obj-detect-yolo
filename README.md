# obj-detect-yolo

Este es un proyecto que integra el modelo YOLOv8 con un chatbot de Telegram para detectar ingredientes en imágenes. Puedes usarlo para identificar ingredientes en fotos y obtener recetas en función de los ingredientes detectados.

## Requisitos

Para utilizar este proyecto, necesitarás:

- Una cuenta de Telegram.
- Acceso al bot de Telegram que se encuentra en este enlace: [enlace del chatbot](https://t.me/IMF_TFM_BOT)

## Instrucciones de Uso

1. **Iniciar el ChatBot**. Busca el ChatBot de Telegram por su nombre de usuario: @IMF_TFM_BOT y ábrelo.

2. **Enviar una foto**. Utiliza la función de enviar fotos de Telegram para enviar una imagen que contenga los ingredientes que quieres identificar. Asegúrate de que los objetos estén claramente visibles en la foto.

3. **Esperar la respuesta**. El ChatBot procesará la imagen y tratará de identificar los ingredientes presentes en ella.

4. **Recibir información**. Una vez que los ingredientes se hayan identificado correctamente, el ChatBot te proporcionará diferentes recetas con esos ingredientes, como su nombre y ubicación en la imagen.

## Tecnología Utilizada

Este proyecto utiliza varias tecnologías para ofrecer sus funciones, incluyendo:

- **Detección de objetos en imágenes**: se utiliza el modelo YOLOv8 pre-entrenado para identificar objetos en las imágenes.

- **API**: utiliza el framework FastAPI con el objetivo de conectar el modelo YOLOv8 con el Chatbot de Telegram alojado en otro repositorio: [enlace al repositorio de Telegram](https://github.com/juankiross/obj-detect-telegram/tree/main).

## Variables de entorno

Para poder ejecutar este proyecto, necesitas configurar las siguientes variables de entorno:

- **WEIGHTS_PATH**: ruta donde se encuentran los pesos del modelo entrenado.

Asegúrate de configurar estas variables de entorno antes de ejecutar el proyecto.

## Limitaciones

Es importante tener en cuenta algunas limitaciones de este proyecto:

- La precisión de la detección de objetos en las imágenes puede variar dependiendo de la calidad de la foto y la visibilidad de los objetos.
- El modelo YOLOv8 puede no reconocer ingredientes no tenidos en cuenta a la hora de entrenar el modelo YOLOv8.
- Este proyecto está diseñado para fines de demostración y puede requerir ajustes adicionales para su implementación en un entorno de producción.
