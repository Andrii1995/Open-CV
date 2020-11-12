import cv2
import numpy as np
img = cv2.imread("lena.png")
kernel = np.ones((3,3),np.uint8)

grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #Градієнт сірого
blur = cv2.GaussianBlur(grey,(3,3),0)   #Розмиття
canny = cv2.Canny(grey,55,100)  #Край
dialation = cv2.dilate(canny,kernel,iterations=1) #Край з багатьма параметрами
eroded = cv2.erode(dialation,kernel,iterations=1)   #Ефект ерозії

#cv2.imshow("Grey",grey)
#cv2.imshow("Blur",blur)
cv2.imshow("Canny",canny)
cv2.imshow("Dialation",dialation)
cv2.imshow("Eroded",eroded)


cv2.waitKey(0)