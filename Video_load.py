import cv2

cap = cv2.VideoCapture("test.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if ord('q') == cv2.waitKey(80) & 0xFF:
        break