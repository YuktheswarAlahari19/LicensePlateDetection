import os
import cv2

def create_output_directory(output_dir):
    os.makedirs(output_dir, exist_ok=True)

def get_image_files(directory):
    return [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

def save_result(img, output_path):
    cv2.imwrite(output_path, img)
