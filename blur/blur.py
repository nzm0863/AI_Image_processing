import cv2

def blur(image, mask, blur_size):
    blurred = cv2.GaussianBlur(image, (blur_size, blur_size), 0)
    image[mask == 255] = blurred[mask == 255]
    return image