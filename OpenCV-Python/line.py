#Program to print a line on an image using opencv tools
import numpy as np
import cv2
# Create a grayscale image or color background of desired intensity
img = np.ones((480,520,3),np.uint8) #Creating a 3D array
b,g,r=cv2.split(img)#Splitting the color channels
img=cv2.merge((10*b,150*g,10*r))#Merging the color channels with modified color channel values
# Draw a diagonal blue line with thickness of 5 px
print img.dtype
print img
cv2.line(img,(0,0),(200,250),(0,0,0),5)#First argument defines the image matrix to which the line has to be added
#Second and third are coordinate points
#Fourth will determine the color of the line which is in matrix form : in BGR Order
#Fifth argument gives the width of the line
cv2.rectangle(img,(20,30),(300,400),(255,255,255),2)
cv2.circle(img,(400,400),40,(0,255,255),4)
pts=np.array([[40,50],[80,90],[60,80],[80,90]],np.int32)
cv2.polylines(img,[pts],False,(0,0,0),3)
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img, 'Hello There!',(200,400),font, 1, (200,150,255),2)
cv2.imshow('image',img)
cv2.waitKey(0)

