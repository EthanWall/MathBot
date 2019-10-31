from PIL import Image
import pytesseract
import cv2

img = cv2.imread(r"images/test1.png")
imgTxt = pytesseract.image_to_string(Image.fromarray(img))

print(imgTxt)

#Change string for math operation
imgTxt = ''.join(imgTxt.split())
imgTxt = imgTxt.lower()
imgTxt = imgTxt.replace("x", "*")
imgTxt = imgTxt.replace("÷", "/")

#Evaluate expression
num = eval(imgTxt)

print(imgTxt)
print(num)