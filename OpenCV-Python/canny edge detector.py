#This program uses the canny algorithm to detect the edges in a video frame
#This program contains the trackbar inputs for higher and lower thresholds for canny algorithm
import cv2
import numpy as np
def nothing(x):
    pass
cap=cv2.VideoCapture(0)
cv2.namedWindow('Threshold')
cv2.createTrackbar('Lower Threshold','Threshold',20, 200,nothing)
cv2.createTrackbar('Higher Threshold','Threshold',20, 200, nothing)
while(True):
    ret, frame=cap.read()
    a=cv2.getTrackbarPos('Lower Threshold','Threshold')
    b=cv2.getTrackbarPos('Higher Threshold','Threshold')
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edge=cv2.Canny(gray,a,b,L2gradient=True)
    cv2.imshow('Original',frame)
    cv2.imshow('Gray Scale',gray)
    cv2.imshow('Edge',edge)
    if cv2.waitKey(1)& 0xff==27:
        break

cap.release()
cv2.destroyAllWindows()
