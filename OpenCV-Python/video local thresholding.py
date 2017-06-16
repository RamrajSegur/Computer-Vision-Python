#This program gives a way to choose the window size of the gaussian threshold and give the result
#Hint: More the window size, more sharper the image is.
import cv2
import numpy as np

print 'Press ESC key to close all the videos'
a=int(raw_input('Give new window size in terms of odd number from 3 to 15'))

cap=cv2.VideoCapture(0)
def nothing(x):
    pass

while(True):
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, a, 2)
    cv2.imshow('gray',gray)
    cv2.imshow('gaussian size7', img3)
    if cv2.waitKey(1) & 0xff==27:
        break

cap.release()
cv2.destroyAllWindows()