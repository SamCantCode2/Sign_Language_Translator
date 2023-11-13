import cv2
import numpy as np
import os
import string

if not os.path.exists("imgs"):
    os.makedirs("imgs")
if not os.path.exists("data/train"):
    os.makedirs("data/train")
if not os.path.exists("data/test"):
    os.makedirs("data/test")
for i in range(9):
    if not os.path.exists("data/train/"+str(i)):
        os.makedirs("data/train/"+str(i))
    if not os.path.exists("data/test/"+str(i)):
        os.makedirs("data/test/"+str(i))
for i in string.ascii_uppercase:
    if not os.path.exists("data/train/"+str(i)):
        os.makedirs("data/train/"+str(i))
    if not os.path.exists("data/test/"+str(i)):
        os.makedirs("data/test/"+str(i))

OP = 'train'
DIR = 'data/'+ OP + '/'
MINVAL = 100

'''
Box Size and thresholding needs work
Might want to change the values
'''
cap = cv2.VideoCapture(0)
stop = -1
while True:
    x, frame = cap.read()
    frame = cv2.flip(frame, 1)
    count = {
        'zero': len(os.listdir(DIR+"/0")),
        'one': len(os.listdir(DIR+"/1")),
        'two': len(os.listdir(DIR+"/2")),
        'three': len(os.listdir(DIR+"/3")),
        'four': len(os.listdir(DIR+"/4")),
        'five': len(os.listdir(DIR+"/5")),
        'six': len(os.listdir(DIR+"/6")),
        'a': len(os.listdir(DIR+"/A")),
        'b': len(os.listdir(DIR+"/B")),
        'c': len(os.listdir(DIR+"/C")),
        'd': len(os.listdir(DIR+"/D")),
        'e': len(os.listdir(DIR+"/E")),
        'f': len(os.listdir(DIR+"/F")),
        'g': len(os.listdir(DIR+"/G")),
        'h': len(os.listdir(DIR+"/H")),
        'i': len(os.listdir(DIR+"/I")),
        'j': len(os.listdir(DIR+"/J")),
        'k': len(os.listdir(DIR+"/K")),
        'l': len(os.listdir(DIR+"/L")),
        'm': len(os.listdir(DIR+"/M")),
        'n': len(os.listdir(DIR+"/N")),
        'o': len(os.listdir(DIR+"/O")),
        'p': len(os.listdir(DIR+"/P")),
        'q': len(os.listdir(DIR+"/Q")),
        'r': len(os.listdir(DIR+"/R")),
        's': len(os.listdir(DIR+"/S")),
        't': len(os.listdir(DIR+"/T")),
        'u': len(os.listdir(DIR+"/U")),
        'v': len(os.listdir(DIR+"/V")),
        'w': len(os.listdir(DIR+"/W")),
        'x': len(os.listdir(DIR+"/X")),
        'y': len(os.listdir(DIR+"/Y")),
        'z': len(os.listdir(DIR+"/Z"))
        }
    xinit = int(0.5*frame.shape[1])
    yinit = 0
    xfinal = frame.shape[1] - 10
    yfinal = int(0.5*frame.shape[0])
    cv2.rectangle(frame, (219, 9), (621, 419), (255, 0, 0), 1)
    roi = frame[10:410, 220:520]
    cv2.imshow("Frame", frame)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 2)
    th = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    ret, test = cv2.threshold(th, MINVAL, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    test = cv2.resize(test, (300, 300))
    cv2.imshow("test", test)
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()