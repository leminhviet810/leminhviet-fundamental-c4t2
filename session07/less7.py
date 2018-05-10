import cv2
import numpy as np

I = cv2.imread("D:\\techkid\\Image processing\\session06\\less6\\shape.jpg")
cv2.imshow("shape",I)


# cách đọc tong máy tính B R G
# extract 3 channel

B = I[:,:,0]
G = I[:,:,1]
R = I[:,:,2]
cv2.imshow("b",B)
cv2.imshow("r",R)
cv2.imshow("g",G)
cv2.waitKey()


C_plus = B&G&R
cv2.imshow("df",C_plus) #1+1 = 1, 1+0 = 0, 0+0 = 0(255(w) = 1, 0(b) = 0)


# convert img to binanry
ret, binImg = cv2.threshold(C_plus, 100, 255,cv2.THRESH_BINARY_INV)
cv2.imshow("bin", binImg)


# find contour
ret, contours, hieracy = cv2.findContours(binImg,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# [cách 1]
# for i in contours:
#     cv2.drawContours(I,i, -1 , (255,0,255), 8)
# cv2.imshow("image contour",I)
#

#cacsh 2

for i in range (len(contours)):
    cv2.drawContours(I ,contours ,i ,(255, 0, 255), 8)
    leni  = cv2.arcLength(contours[i], True)
    areai = cv2.contourArea(contours[i], False)
    print("area",areai)
    print("len",leni)
    #appoximate polygon
    nedges = cv2.approxPolyDP(contours[i], 5 ,True) #5 = sai só của tâm contour đến rìa của hình thật
    print ("polyedeges ", len(nedges))
    if (len(nedges)) == 3:
        cv2.putText(I,"tam giac", (nedges[1][0][0], nedges[1][0][1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0))
    if (len(nedges)) == 4:
        cv2.putText(I,"hcn", (nedges[0][0][0], nedges[0][0][1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0))
    if (len(nedges)) >= 8:
        cv2.putText(I,"tron", (nedges[0][0][0], nedges[0][0][1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0))
    M = cv2.moments(contours[i])
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.circle(I, (cx, cy) ,10, (120,255,0), 5)
cv2.namedWindow("con tua", cv2.WINDOW_NORMAL)
cv2.imshow("con tua", I)
cv2.waitKey()
