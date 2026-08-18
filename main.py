from ultralytics import YOLO
from pathlib import Path
from shutil import move
from get_image import get_image_files
from detector import detect
# from move_image import move_image
from save_image import save_image
import cv2

# model = YOLO("yolo11n-seg.pt")
# MODEL_PATH = "runs/segment/train-9/weights/best.pt"
# MODEL_PATH = "models/best.pt"
# model = YOLO(MODEL_PATH)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "best.pt"

model = YOLO(str(MODEL_PATH))

def process_images(
    input_dir,
    output_dir,
    blur_size,
    confidence,
    progress_callback=None,
    log_callback=None
):
    def log(message):
        if log_callback:
            log_callback(message)
        else:
            print(message)
            
    extensions = ["*.png", "*.jpg", "*.jpeg", "*.webp"]
    # input_dir = Path("input")
    image_files = get_image_files(input_dir, extensions)

    # output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    count = 0
    saved = 0
    no_detection = 0

    total = len(image_files)
    for current, image_path in enumerate(image_files, start=1):
        count += 1

        log(f"{image_path.name} ... 処理中")
        
        image = cv2.imread(str(image_path))
        image, detected = detect(image, model,blur_size,confidence)

        if not detected:
            no_detection += 1
            log(f"{image_path.name}: 検出なし")

        if save_image(output_dir, image_path, image):
            saved += 1

        log(f"{image_path.name} 完了")
        
        # move_image(image_path)
                
        if progress_callback:
            progress_callback(current, total)
        
        
        log(f"[{count}] {image_path.name}")
        
        
    log("すべての画像の処理が完了しました！")
    log(f"検出なし: {no_detection}")
    log(f"対象画像: {len(image_files)}枚")
    log(f"処理枚数: {count}")
    log(f"保存枚数: {saved}")
    
