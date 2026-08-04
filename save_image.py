import cv2

def save_image(output_dir,image_path,image):
    output_path = output_dir / image_path.name
    return cv2.imwrite(str(output_path), image)