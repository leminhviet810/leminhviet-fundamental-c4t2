import numpy as np
import cv2

# connect webcam]
cap = cv2.VideoCapture(0)
lower = np.array([0,30,23])
higher = np.array([137,255,215])
while True:
    ret,frame = cap.read()
    hsvImg= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # convrt to binary
    BinImage = cv2.inRange(hsvImg,lower,higher)
    cv2.imshow("bin", BinImage)
    cv2.imshow("vid0",frame)
    cv2.imshow("vid", hsvImg)
    key = cv2.waitKey(30)
    if key == ord('q'):
        break