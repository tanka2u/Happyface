import cv2
import numpy as np
from PIL import Image

image_path = 'avatar.png'
image = cv2.imread(image_path)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

mask = np.zeros_like(image)

for (x, y, w, h) in faces:
    center = (x + w // 2, y + h // 2)
    radius = max(w, h) // 2
    cv2.circle(mask, center, radius, (255, 255, 255), -1)

result = cv2.bitwise_and(image, mask)

output_path = 'path_to_save_image.png'
cv2.imwrite(output_path, result)

def convertImage(output_path):
    img = Image.open(output_path)
    img = img.convert("RGBA")
 
    datas = img.getdata()
 
    newData = []
 
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
 
    img.putdata(newData)
    img.save("./New.png", "PNG")
    print("Successful")
    
def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print(f"The original image size is {width} wide x {height} high")

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print(f"The resized image size is {width} wide x {height} high")

    resized_image.save(output_image_path)
    
input_image = 'avatar.png' 
output_image = 'resized_image.png'
size = (512, 512)

resize_image(output_path, output_image, size)
convertImage(output_image)

# 
# def make_badge(outpath):
    # return output_path
# image_path = './avatar.png'
# badge = make_badge(image_path)
# transparentImage = convertImage(badge)
# resized_image = resize_image(transparentImage)
# validate(resize_image)