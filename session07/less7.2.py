import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("D:\\techkid\\Image Processing\\session07\\tai_lieu\\haarcascade_frontalface_alt2.xml")
mask = cv2.imread("D:\\techkid\\Image Processing\\session07\\tai_lieu\\con_meo.jpg")


while (True):
    ret,frame = cap.read()
    # convert image to gray
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    faces = cascade.detectMultiScale(gray)
    for x,y,w,h in faces:
        remask = cv2.resize(mask,(w,h), cv2.INTER_CUBIC)
        cv2.rectangle(frame, (x,y), (x+w, y+h) ,(0,0,255), 2)
        frame[y:y+h, x:x+w, :] = remask
    cv2.imshow("vid", frame)
    key = cv2.waitKey(30)
    if key == ord('q'):
        break
# x : col, y = row ( row trước col)