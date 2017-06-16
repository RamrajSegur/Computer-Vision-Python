#This program is about zooming a video captured using the camera using the sliders in opencv
#Here Opencv function resize is used
import cv2
import numpy as np

def nothing(x):
    pass
cap=cv2.VideoCapture(0)

cv2.namedWindow('Zoom slider')
cv2.createTrackbar('Slide','Zoom slider',1,3,nothing)

while(True):
    ret,img=cap.read()
    a=cv2.getTrackbarPos('Slide','Zoom slider')
    res=cv2.resize(img,None,fx=a,fy=a,interpolation=cv2.INTER_CUBIC)
    cv2.imshow('original',img)
    cv2.imshow('transformed',res)
    if  cv2.waitKey(1) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()