import shutil
import random
import json
from pathlib import Path

random.seed(42)

# クラス名
CLASS_NAMES = {
    "target": 0
}

images_dir = Path("fail_images")
dataset_dir = Path("dataset")

train_images = dataset_dir / "images" / "train"
val_images = dataset_dir / "images" / "val"

train_labels = dataset_dir / "labels" / "train"
val_labels = dataset_dir / "labels" / "val"


train_images.mkdir(parents=True, exist_ok=True)
val_images.mkdir(parents=True, exist_ok=True)

train_labels.mkdir(parents=True, exist_ok=True)
val_labels.mkdir(parents=True, exist_ok=True)



for json_file in images_dir.glob("*.json"):

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    if random.random() < 0.8:
        image_dst = train_images
        label_dst = train_labels
    else:
        image_dst = val_images
        label_dst = val_labels
    


    width = data["imageWidth"]
    height = data["imageHeight"]

    output = []

    for shape in data["shapes"]:

        label = shape["label"]

        if label not in CLASS_NAMES:
            continue

        class_id = CLASS_NAMES[label]

        line = [str(class_id)]

        for x, y in shape["points"]:
            line.append(f"{x / width:.6f}")
            line.append(f"{y / height:.6f}")

        output.append(" ".join(line))

    txt_path = label_dst / (json_file.stem + ".txt")
    
    image_path = images_dir / data["imagePath"]

    if image_path.exists():
        shutil.copy(image_path, image_dst / image_path.name)
    else:
        print(f"画像が見つかりません: {image_path}")

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output))

    print(f"変換完了: {txt_path.name}")

print("すべて変換しました！")