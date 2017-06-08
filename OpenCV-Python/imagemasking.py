import cv2
import numpy as np

img1=cv2.imread('/home/ramraj/Downloads/messi.jpg',0)#Image that is going to be on background
img=cv2.imread('/home/ramraj/Downloads/mainlogo.png',0)#Image that is going to be on foreground
rows,columns=img.shape
roi=img1[0:rows,0:columns]#Making the region on interest
ret,img_thres=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)#Making the mask for foreground image
img_thres_inv=cv2.bitwise_not(img_thres)#Making the mask for background image
img_3=cv2.bitwise_and(roi,roi,mask=img_thres_inv)#Making the pixels transparent on the region where the foreground image will come
img_4=cv2.bitwise_and(img,img,mask=img_thres)#Making the pixels transparent on the region where the background image will come
img_5=cv2.add(img_3,img_4)#Blending two regions
img1[0:rows,0:columns]=img_5#Adding the blended region to the image
cv2.imshow("Image_blended",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()