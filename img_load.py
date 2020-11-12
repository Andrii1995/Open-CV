import cv2
print("All is OK")

img = cv2.imread("lena.png")
cv2.imshow("LENA", img)
cv2.waitKey(0)