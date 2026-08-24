from ultralytics import YOLO
from utils.resource import resource_path
from pathlib import Path
import numpy as np
import cv2

MODEL_PATH = resource_path("models/best.pt")

model = YOLO(str(MODEL_PATH))

def detect(image,confidence):
    # AIで検出
    results = model(image, conf=confidence)
    result = results[0]

    # 検出なし
    if result.masks is None:
        empty_mask = np.zeros(image.shape[:2], dtype=np.uint8)
        return empty_mask, False
    # マスク作成
    masks = results[0].masks
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    for polygon in masks.xy:
        polygon = polygon.astype(np.int32)
        cv2.fillPoly(mask, [polygon], 255)

    return mask, True