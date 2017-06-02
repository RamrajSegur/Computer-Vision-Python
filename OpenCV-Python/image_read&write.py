import numpy as np
import cv2
import time
#Reading the image from local memory in different formats
img = cv2.imread('/home/ramraj/Downloads/messi.jpg',0)#Grayscale
img1=cv2.imread('/home/ramraj/Downloads/messi.jpg',1)#Alphacolor
img2=cv2.imread('/home/ramraj/Downloads/messi.jpg',-1)#BGR - In python BGR is used instead of RGB
#displaying the images
cv2.imshow('image',img)
cv2.imshow('alpha',img1)
cv2.imshow('color',img2)
#verifying the image data
print img[400,500]
print img1[400,500]
#Saving the images to local memory
cv2.imwrite('/home/ramraj/image/colorimagemessi.jpg',img2)
cv2.imwrite('/home/ramraj/image/alphaimage.jpg',img1)
cv2.imwrite('/home/ramraj/image/blackandwhite.jpg',img)
start=time.time()
cv2.waitKey(0) #Wait for keyboard input to close all the image windows
cv2.destroyAllWindows()
