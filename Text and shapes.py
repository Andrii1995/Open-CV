import cv2
import numpy as np

img = np.zeros((512,512,3),)
#img[0:100,200:500]= 255,0,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),1)
cv2.rectangle(img,(20,20),(492,492),(100,100,0),cv2.FILLED)
cv2.circle(img,(256,256),75,(11,11,11),4)
cv2.putText(img,"SuperMario",(100,100),cv2.FONT_HERSHEY_PLAIN,4,(0,0,255),5)
cv2.imshow("BLACK",img)
cv2.waitKey(0)