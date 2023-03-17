from imageai.Detection import ObjectDetection
from PIL import Image
import os
import urllib3
import shutil


class AIManager:

    def __init__(self):
        self.name = "AI"
        self.__model_path = 'yolov3.pt'

        self.__download_model()

        self.detector = ObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath(self.__model_path)
        self.detector.loadModel()

    def __download_model(self):
        url_model = 'https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt/'

        if os.path.exists(self.__model_path):
            return

        http = urllib3.PoolManager()
        with open(self.__model_path, "wb") as out:
            r = http.request('GET', url_model, preload_content=False)
            shutil.copyfileobj(r, out)

    def detect(self, img_path):
        try:
            detections = self.detector.detectObjectsFromImage(img_path, "image_new.jpg", minimum_percentage_probability=30)
        except AttributeError:
            with Image.open(img_path) as im:
                im.save('image_new.jpg')

    def detect_api(self, img_path):
        detected_items = []

        try:
            detections = self.detector.detectObjectsFromImage(img_path, "image_new_api.jpg", minimum_percentage_probability=30)

            for eachObject in detections:
                detected_item = {}
                detected_item["name"] = eachObject["name"]
                detected_item["percentage_probability"] = eachObject["percentage_probability"]

                detected_items.append(detected_item)
        except AttributeError:
            pass

        return detected_items
