import numpy as np
import cv2

cap = cv2.VideoCapture(1) # Argument 1 - read the image from a USB Camera

while(True):#Alternatively while(cap.isOpened()) can be used to check the working of camera
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print "I am executing"
    # Display the resulting frame
    cv2.imshow('grayscale',gray)
    cv2.imshow('color',frame)
    # Waiting for the keyboard key 'q' to quit the image windows
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

#Problem encountered :
# error: "(-215) size.width>0 && size.height>0 in function imshow" shown up
# because of the connection problem of camera with USB
