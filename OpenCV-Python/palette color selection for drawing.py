#This program is used to select a particular by choosing the RGB values using the slider and draw the same in a separate window
#It is also having option to choose the desired radius of the circle
import cv2
import numpy as np

def nothing(x):
    pass
def mousecallback(event,x,y,flags,param):#Mouse event callback function
    if event==cv2.EVENT_LBUTTONDOWN:#Left mouse button down can be taken as an event
        cv2.circle(img1,(x,y),radius,(b,g,r),-1) #the circle's color is assigned by taking the values from slider (b,g,r)

img=np.zeros((10,10,3),np.uint8) #Creating a window for the trackbar and the sample color palette
cv2.namedWindow('Color palette')

cv2.createTrackbar('R','Color palette',0,255,nothing)#Trackbars for R,G and B & Radius of the circle
cv2.createTrackbar('G','Color palette',0,255,nothing)
cv2.createTrackbar('B','Color palette',0,255,nothing)
cv2.createTrackbar('Rad','Color palette',0,100,nothing)

img1=np.ones((512,512,3),np.uint8)#Creating the white canvas screen
img1=255*img1
cv2.namedWindow('Canvas')

cv2.setMouseCallback('Canvas',mousecallback)

print "Press 'ESC' key to close all the windows"

switch='0:OFF \n 1: ON' #Creating the switch for color selection
cv2.createTrackbar(switch,'Color palette',0,1,nothing)

while(1):
    cv2.imshow('Color palette',img)
    cv2.imshow('Canvas',img1)
    k=cv2.waitKey(1)& 0xFF
    if k==27: #Waiting for the Escape key
        break
    r=cv2.getTrackbarPos('R','Color palette') #Getting the tracker values
    g=cv2.getTrackbarPos('G','Color palette')
    b=cv2.getTrackbarPos('B','Color palette')
    s=cv2.getTrackbarPos(switch,'Color palette')
    radius=cv2.getTrackbarPos('Rad','Color palette')
    if s==0: #Getting the switch position value
        img[:]=0
    else:
        img[:]=[b,g,r] #Making the sample color palette window

cv2.destroyAllWindows()


