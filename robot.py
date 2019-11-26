from PIL import Image
import pytesseract
from cv2 import cv2

img = cv2.imread(r"images/test1.png")
imgTxt = pytesseract.image_to_string(Image.fromarray(img))

print(imgTxt)

#Change string for math operation
imgTxt = imgTxt.lower()
imgTxt = imgTxt.replace("x", "*")
imgTxt = imgTxt.replace("÷", "/")
imgTxt = ''.join(i for i in imgTxt if i.isdigit() or i == "*" or i == "/" or i == "+" or i == "-")

#Evaluate expression
try:
    num = eval(imgTxt)
except:
    print("Evaluating expression failed, terminating!")
    exit()

print(imgTxt)
print(num)