from PIL import Image
import pytesseract

imageText = pytesseract.image_to_string(Image.open("images/test.png"))

print(imageText)