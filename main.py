from PIL import Image
import numpy as np

def is_within_circle(x, y, center, radius):
    return (x - center)**2 + (y - center)**2 <= radius**2

def is_happy_color(rgb):
    r, g, b = rgb
    return r > 150 and g > 150 and b > 100 # my happy criteria

def validate_badge(image_path):
    try:
        image = Image.open(image_path).convert("RGBA")
        
        if image.size != (512, 512): # checking size
            return False, "Image size is not 512x512"

        data = np.array(image) # Get image data
        height, width, _ = data.shape
        center = height // 2
        radius = center

        for y in range(height):
            for x in range(width):
                r, g, b, a = data[y, x]
                if a != 0:  
                    if not is_within_circle(x, y, center, radius):
                        return False, "Non-transparent pixels are outside the circle"
                    if not is_happy_color((r, g, b)):
                        return False, "Colors are not 'happy'"
        return True, "The badge is valid"
    except Exception as e:
        return False, str(e)

valid, message = validate_badge("./New.png")
print(message)
