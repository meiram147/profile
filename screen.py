import pyautogui as pg 
import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image


pg.screenshot('screenshot.png',region=(1400,59, 200, 30)) 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
image = cv2.imread("screenshot.png")
string = pytesseract.image_to_string(image)
string1= string.replace(' ', '')
s = string1[1:]
try:
    s = int(s)
    if s == 9309706:
        print("это Медет")
    else:
        print(s,"не знакомый номер")
except ValueError:
    print("ошибка это твой кореш") 
