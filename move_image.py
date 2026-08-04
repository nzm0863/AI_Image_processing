from pathlib import Path
from shutil import move

processed_dir = Path("processed")
processed_dir.mkdir(exist_ok=True)

def move_image(image_path):
    move(str(image_path), str(processed_dir / image_path.name))