import cv2


cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.5, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 4)
        cv2.imshow("Video", img)
    if ord('q') == cv2.waitKey(1) & 0xFF:
       break






