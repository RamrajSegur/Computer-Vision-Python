#This program is about zooming an image using the sliders in opencv
#Here Opencv function resize is used
import cv2
import numpy as np

def nothing(x):
    pass
img=cv2.imread('/home/ramraj/Downloads/messi.jpg')

cv2.namedWindow('Zoom slider')
cv2.createTrackbar('Slide','Zoom slider',1,3,nothing)

while(1):
    a=cv2.getTrackbarPos('Slide','Zoom slider')
    res=cv2.resize(img,None,fx=a,fy=a,interpolation=cv2.INTER_CUBIC)
    cv2.imshow('original',img)
    cv2.imshow('transformed',res)
    if  cv2.waitKey(0)&0xff == 27:
        break

cv2.destroyAllWindows()