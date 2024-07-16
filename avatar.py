import cv2
import numpy as np
from PIL import Image

def detect_and_mask_faces(image_path):
    image = cv2.imread(image_path)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    mask = np.zeros_like(image)
    
    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        radius = max(w, h) // 2
        cv2.circle(mask, center, radius, (255, 255, 255), -1)
    
    result = cv2.bitwise_and(image, mask)
    return result

def save_image(image, output_path):
    cv2.imwrite(output_path, image)

def convert_image_to_rgba(input_path, output_path):
    img = Image.open(input_path)
    img = img.convert("RGBA")
    datas = img.getdata()
    new_data = [(255, 255, 255, 0) if item[0] == 0 and item[1] == 0 and item[2] == 0 else item for item in datas]
    img.putdata(new_data)
    img.save(output_path, "PNG")
    print("Image conversion to RGBA completed successfully.")

def resize_image(input_path, output_path, size):
    original_image = Image.open(input_path)
    resized_image = original_image.resize(size)
    resized_image.save(output_path)
    print(f"Image resized to {size} and saved to {output_path}.")

if __name__ == "__main__":
    input_image_path = 'avatar.png'
    masked_image_path = 'masked_image.png'
    resized_image_path = 'resized_image.png'
    final_image_path = 'final_image.png'
    
    masked_image = detect_and_mask_faces(input_image_path)
    save_image(masked_image, masked_image_path)
    
    resize_size = (512, 512)
    resize_image(masked_image_path, resized_image_path, resize_size)
    
    convert_image_to_rgba(resized_image_path, final_image_path)
