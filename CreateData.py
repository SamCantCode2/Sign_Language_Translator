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
for i in range(10):
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

cap = cv2.VideoCapture(0)
stop = -1
while True:
    x, frame = cap.read()
    frame = cv2.flip(frame, 1)
    count = {
        '0': len(os.listdir(DIR+"/0")),
        '1': len(os.listdir(DIR+"/1")),
        '2': len(os.listdir(DIR+"/2")),
        '3': len(os.listdir(DIR+"/3")),
        '4': len(os.listdir(DIR+"/4")),
        '5': len(os.listdir(DIR+"/5")),
        '6': len(os.listdir(DIR+"/6")),
        '7': len(os.listdir(DIR+"/7")),
        '8': len(os.listdir(DIR+"/8")),
        '9': len(os.listdir(DIR+"/9")),
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
    cv2.rectangle(frame, (419, 9), (721, 204), (255, 0, 0), 1)
    roi = frame[10:205, 420:720]
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
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(DIR+'0/'+str(count['0'])+'.jpg', test)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(DIR+'1/'+str(count['1'])+'.jpg', test)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(DIR+'2/'+str(count['2'])+'.jpg', test)       
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(DIR+'3/'+str(count['3'])+'.jpg', test)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(DIR+'4/'+str(count['4'])+'.jpg', test)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(DIR+'5/'+str(count['5'])+'.jpg', test)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(DIR+'6/'+str(count['6'])+'.jpg', test)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(DIR+'7/'+str(count['7'])+'.jpg', test)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(DIR+'8/'+str(count['8'])+'.jpg', test)
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite(DIR+'9/'+str(count['9'])+'.jpg', test)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(DIR+'A/'+str(count['a'])+'.jpg', test)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(DIR+'B/'+str(count['b'])+'.jpg', test)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(DIR+'C/'+str(count['c'])+'.jpg', test)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(DIR+'D/'+str(count['d'])+'.jpg', test)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(DIR+'E/'+str(count['e'])+'.jpg', test)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(DIR+'F/'+str(count['f'])+'.jpg', test)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(DIR+'G/'+str(count['g'])+'.jpg', test)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(DIR+'H/'+str(count['h'])+'.jpg', test)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(DIR+'I/'+str(count['i'])+'.jpg', test)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(DIR+'J/'+str(count['j'])+'.jpg', test)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(DIR+'K/'+str(count['k'])+'.jpg', test)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(DIR+'L/'+str(count['l'])+'.jpg', test)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(DIR+'M/'+str(count['m'])+'.jpg', test)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(DIR+'N/'+str(count['n'])+'.jpg', test)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(DIR+'O/'+str(count['o'])+'.jpg', test)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(DIR+'P/'+str(count['p'])+'.jpg', test)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(DIR+'Q/'+str(count['q'])+'.jpg', test)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(DIR+'R/'+str(count['r'])+'.jpg', test)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(DIR+'S/'+str(count['s'])+'.jpg', test)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(DIR+'T/'+str(count['t'])+'.jpg', test)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(DIR+'U/'+str(count['u'])+'.jpg', test)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(DIR+'V/'+str(count['v'])+'.jpg', test)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(DIR+'W/'+str(count['w'])+'.jpg', test)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(DIR+'X/'+str(count['x'])+'.jpg', test)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(DIR+'Y/'+str(count['y'])+'.jpg', test)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(DIR+'Z/'+str(count['z'])+'.jpg', test)
cap.release()
cv2.destroyAllWindows()
