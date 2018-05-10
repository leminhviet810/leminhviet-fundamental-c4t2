import cv2
import numpy as np
I = cv2.imread("D:\\techkid\\Image processing\\session06\\less6\\noise_house.jpg")

[rows, cols, chan] = I.shape
for i in range(rows -1):
    for j in range(cols - 1):
        for k in range (chan):
            print (i)
            x = [I[i+1,j,k], I[i-1,j,k], I[i,j+1,k],I[i,j-1,k]]
            if I[i,j,k] < np.median(x) or I[i,j,k] >np.median(x):
                I[i,j,k] = np.median(x)
cv2.imshow("i", I)
cv2.waitKey()