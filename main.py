from pathlib import Path
from shutil import move
from get_image import get_image_files
from detector.private_parts import detect as private_parts_detect
from detector.face import detect as face_detect
from blur import blur
# from move_image import move_image
from save_image import save_image
import cv2

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
    parts=["private_parts","face"]
    detectors = {
        "private_parts": private_parts_detect,
        "face": face_detect,
    }
    # input_dir = Path("input")
    image_files = get_image_files(input_dir, extensions)

    # output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    count = 0
    saved = 0
    no_detection = 0

    total = len(image_files)
    
    
    for current, image_path in enumerate(image_files, start=1):
        combined_mask = None
        image_detected = False
        count += 1

        log(f"{image_path.name} ... 処理中")
        
        image = cv2.imread(str(image_path))
        
        
        for part in parts:
            detector = detectors[part]

            mask, detected = detector(image, confidence)

            if detected:  
                image_detected = True

                if combined_mask is None:
                    combined_mask = mask
                else:
                    combined_mask = cv2.bitwise_or(combined_mask, mask)
                
        # 最後に1回だけぼかす
        if combined_mask is not None:
            image = blur(image, combined_mask, blur_size)
            
        if not image_detected:
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
    
