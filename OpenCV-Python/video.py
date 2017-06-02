import numpy as np
import cv2
import time

cap = cv2.VideoCapture(1)
#time.sleep(2)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print "I am executing"
    # Display the resulting frame
    cv2.imshow('grayscale',gray)
    cv2.imshow('color',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
