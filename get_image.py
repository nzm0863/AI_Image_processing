from pathlib import Path


def get_image_files(input_dir, extensions):
    image_files = []

    for ext in extensions:
        image_files.extend(input_dir.glob(ext))
    
    return image_files
    