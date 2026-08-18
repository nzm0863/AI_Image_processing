from ultralytics import YOLO
# from pathlib import Path
# from shutil import move
import cv2

# processed_dir = Path("processed")
# processed_dir.mkdir(exist_ok=True)


def detect(image,model,blur_size,confidence):

    # AIで検出
    results = model(image, conf=confidence)

    masks = results[0].masks
    
    if masks is None:
        print("検出なし")
        return image, False

    mask = image.copy()
    mask[:] = 0
    
    for i, polygon in enumerate(masks.xy):
        polygon = polygon.astype("int32")
        cv2.fillPoly(mask, [polygon], (255,255,255))
            
    # for i, polygon in enumerate(masks.xy):
    #     print(type(polygon))
    #     print(polygon)
    #     break
        
    # 全体をぼかす
    blur = cv2.GaussianBlur(image, (blur_size, blur_size), 0)

    # 白い部分だけ置き換える
    image[mask == 255] = blur[mask == 255]
    
    
    
    return image, True
