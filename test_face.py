import cv2
from pathlib import Path
MODEL_PATH = "models/face_detection_yunet_2026may.onnx"
IMAGE_PATH = "images/sample.jpg"

image = cv2.imread(IMAGE_PATH)

BASE_DIR = Path(__file__).resolve().parent

height, width = image.shape[:2]

detector = cv2.FaceDetectorYN.create(
    MODEL_PATH,
    "",
    (width, height),
    score_threshold=0.4,
    nms_threshold=0.3,
    top_k=5000,
)

detector.setInputSize((width, height))

_, faces = detector.detect(image)

if faces is None:
    print("顔が見つかりません")
else:
    print(f"顔検出数: {len(faces)}")
    
    blur = cv2.GaussianBlur(
        image,
        (51, 51),
        0
    )

    for face in faces:
        x, y, w, h = face[:4]

        x = int(x)
        y = int(y)
        w = int(w)
        h = int(h)

        image[y:y+h, x:x+w] = blur[y:y+h, x:x+w]

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2,
        )

cv2.imwrite(
    str(BASE_DIR / "images" / "face_blur_test.jpg"),
    image
)