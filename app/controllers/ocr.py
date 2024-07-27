from PIL import Image
from pytesseract import image_to_string

def ocr_extraction(image_path):
    image = Image.open(image_path)
    text = image_to_string(image)
    return text

