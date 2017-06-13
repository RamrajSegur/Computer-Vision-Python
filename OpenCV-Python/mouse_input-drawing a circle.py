#This program is about drawing a circle at the poin on screen where we single click on mouse
import cv2
import numpy as np

# Function will be called whenever there is a mouse movement/event happens see the line number 17
def draw_circle(event,x,y,flags,param): #These are the default arguments that are passed in the setMouseCallback function
    # To check the desired event happened. cv2.EVENT_LBUTTONDOWN is left mouse button down/click event
    #There are also lot of events we can compare through like left button double click, left button up,
    # same events also avialable for the right mouse button keys
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),-1)#The blue filled circle is drawn at the mouse selected points

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)#This line created the black screen of size 512x512
cv2.namedWindow('image') # This line gives the name to the window (black screen created)
# This line sets the default mouse call back function until the program runs
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27: #This line defines the 'esc' key that is used to close the current image window
        break
cv2.destroyAllWindows()
