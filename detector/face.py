from pathlib import Path
import numpy as np
import cv2

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "face_detection_yunet_2026may.onnx"

detector = cv2.FaceDetectorYN.create(
    str(MODEL_PATH),
    "",
    (320, 320),  # 初期値。後で画像サイズに合わせる。
)

def detect(image, confidence):
    detector.setScoreThreshold(confidence)
    h, w = image.shape[:2]
    detector.setInputSize((w, h))

    _, faces = detector.detect(image)

    if faces is None:
        return None, False

    mask = np.zeros(image.shape[:2], dtype=np.uint8)

    for face_data in faces:
        x, y, fw, fh = face_data[:4].astype(int)
        margin = 0.2

        x = max(0, int(x - fw * margin))
        y = max(0, int(y - fh * margin))

        fw = min(w - x, int(fw * (1 + margin * 2)))
        fh = min(h - y, int(fh * (1 + margin * 2)))

        cv2.rectangle(mask, (x, y), (x + fw, y + fh), 255, -1)

    return mask, True