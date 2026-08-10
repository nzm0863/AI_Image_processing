from ultralytics import YOLO
from pathlib import Path
from shutil import move
from get_image import get_image_files
from detector import detect
# from move_image import move_image
from save_image import save_image
import cv2

# model = YOLO("yolo11n-seg.pt")
# MODEL_PATH = "runs/segment/train-8/weights/best.pt"
MODEL_PATH = "models/train8-best.pt"
model = YOLO(MODEL_PATH)

def process_images(
    input_dir,
    output_dir,
    blur_size,
    confidence
):
    extensions = ["*.png", "*.jpg", "*.jpeg", "*.webp"]
    # input_dir = Path("input")
    image_files = get_image_files(input_dir, extensions)

    # output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    count = 0
    saved = 0

    no_detection = 0


    for image_path in image_files:
        count += 1

        print(f"{image_path.name} ... 処理中")
        
        image = cv2.imread(str(image_path))
        image, detected = detect(image, model,blur_size,confidence)

        if not detected:
            no_detection += 1
            print(f"{image_path.name}: 検出なし")

        if save_image(output_dir, image_path, image):
            saved += 1

        print(f"{image_path.name} 完了")
        
        # move_image(image_path)
        
        
        print(f"[{count}] {image_path.name}")
        
        
    print("すべての画像の処理が完了しました！")
    print(f"検出なし: {no_detection}")
    print(f"対象画像: {len(image_files)}枚")
    print(f"処理枚数: {count}")
    print(f"保存枚数: {saved}")