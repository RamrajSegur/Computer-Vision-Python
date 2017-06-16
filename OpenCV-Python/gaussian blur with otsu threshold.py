# This program uses the global thresholding
# It uses the otsu thresholding method to get the threshold value automatically
import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while(True):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blurred=cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh=cv2.threshold(blurred,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('Gray',gray)
    cv2.imshow('Blurred',blurred)
    cv2.imshow('Otsu',thresh)
    if cv2.waitKey(1)& 0xff==27:
        break

cap.release()
cv2.destroyAllWindows()
