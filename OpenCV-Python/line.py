#Program to print a line on an image using opencv tools in python
import numpy as np
import cv2
# Create a grayscale image or color background of desired intensity
img = np.ones((480,520,3),np.uint8) #Creating a 3D array
img1=10*img[:,:,0]#Defining the blue color intensity
img2=150*img[:,:,1]#Defining the green color intensity
img3=10*img[:,:,2]#Defining the red color intensity
img=np.dstack((img1,img2,img3))#Combining the individual intensity matrices into a single BGR matrix
# Draw a diagonal blue line with thickness of 5 px
print img.dtype
print img
cv2.line(img,(0,0),(200,250),(0,0,0),5)#First argument defines the image matrix to which the line has to be added
#Second and third are coordinate points
#Fourth will determine the color of the line which is in matrix form : in BGR Order
#Fifth argument gives the width of the line
cv2.imshow('image',img)
cv2.waitKey(0)
