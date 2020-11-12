import cv2
import numpy as np

img = cv2.imread("cards.png")

width, height = 250,350
pts1 = np.float32([[269,30],[507,110],[173,426],[419,511]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
img = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Cards",img)
cv2.waitKey(0)