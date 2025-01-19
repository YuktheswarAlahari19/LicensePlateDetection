from ultralytics import YOLO
import easyocr

def load_model(model_path):
    return YOLO(model_path)

def initialize_ocr():
    return easyocr.Reader(['en'])
