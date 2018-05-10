import cv2
import numpy as np
i = cv2.imread("D:\\techkid\\Image processing\\session06\\less6\\erosion.jpg")
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
bin_erode = cv2.erode(i, kernel)
final = cv2.dilate(bin_erode, kernel)
cv2.imshow("final", final)
cv2.waitKey()
