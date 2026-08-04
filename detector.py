from ultralytics import YOLO
from pathlib import Path
from shutil import move
import cv2

processed_dir = Path("processed")
processed_dir.mkdir(exist_ok=True)

BLUR_SIZE = 31
CONFIDENCE = 0.4

def detect(image,model):

    # AIで検出
    results = model(image)

    masks = results[0].masks
    
    if masks is None:
        print("検出なし")
        return image, False

    mask = image.copy()
    mask[:] = 0
    
    for i, polygon in enumerate(masks.xy):

        conf = results[0].boxes.conf[i]

        if conf < CONFIDENCE:
            continue

        polygon = polygon.astype("int32")
        cv2.fillPoly(mask, [polygon], (255,255,255))
        print(f"conf={conf:.2f}")
        
    # 全体をぼかす
    blur = cv2.GaussianBlur(image, (BLUR_SIZE, BLUR_SIZE), 0)

    # 白い部分だけ置き換える
    image[mask == 255] = blur[mask == 255]
    return image, True
