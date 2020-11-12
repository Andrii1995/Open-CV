import cv2

img = cv2.imread("photo1.jpg")
resize = cv2.resize(img,(480,640))#Resize
cropp = img[204:548,102:380] #Cropp


# cv2.imshow("IMG",img)
# cv2.imshow("IMG RESIZE",resize)
cv2.imshow("IMG CROPPED",cropp)
# print(img.shape)
# print(resize.shape)
cv2.waitKey(0)
cv2.imwrite("photo3.jpg",cropp)