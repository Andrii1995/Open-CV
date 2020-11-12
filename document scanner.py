import cv2
import numpy as np


imgWidth = 1280
imgHeight = 960


framew = 1280
frameh = 960
cap = cv2.VideoCapture(0)
cap.set(3, framew)
cap.set(4,frameh)
kernel = np.ones((5,5),np.uint8)
cap.set(10,150)

def Preprocessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    imgdialate = cv2.dilate(imgCanny,kernel,iterations = 2)
    imgThres = cv2.erode(imgdialate,kernel,iterations=1)
    return imgThres


def getContours(img):
    biggest = np.array([])
    Maxarea = 0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            #cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area>Maxarea & len(approx) == 4:
                biggest = approx
                Maxarea = area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 15)
    return biggest

def reorder(Mypoint):
    Mypoint = Mypoint.reshape((4,2))
    mynewpoint = np.zeros((4,1,2),np.int32)
    add = Mypoint.sum(1)
    print("ADD",add)

    mynewpoint[0] = Mypoint[np.argmin(add)]
    mynewpoint[3] = Mypoint[np.argmax(add)]
    diff = np.diff(Mypoint,axis = 1 )
    mynewpoint[1] = Mypoint[np.argmin(diff)]
    mynewpoint[2] = Mypoint[np.argmax(diff)]

    return mynewpoint

def getWarp(img,biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [imgWidth, 0], [0, imgHeight], [imgWidth, imgHeight]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOut = cv2.warpPerspective(img, matrix, (imgWidth, imgHeight))

    return imgOut

while True:
    success, img = cap.read()
    cv2.resize(img,(imgWidth,imgHeight))
    imgContour = img.copy()
    imgThres = Preprocessing(img)
    biggest = getContours(imgThres)
    imgWarp = getWarp(img,biggest)
    cv2.imshow("Start", imgWarp)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break