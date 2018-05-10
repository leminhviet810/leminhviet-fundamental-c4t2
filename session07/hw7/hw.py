import cv2

I = cv2.imread("D:\\techkid\\Image processing\\session06\\less6\\shape.jpg")
[rows, cols, c] = I.shape
def bin(x):
    for i in range(rows):
        for j in range(cols):
            if I[i,j,0] > 200 and I[i,j,1] > 200 and I[i,j,2] > 200 :
                I[i,j,:] = 0
    B = I[:,:,0]
    G = I[:,:,1]
    R = I[:,:,2]
    _,bin_B = cv2.threshold(B,200,255,cv2.THRESH_BINARY)
    _,bin_G = cv2.threshold(G,200,255,cv2.THRESH_BINARY)
    _,bin_R = cv2.threshold( R, 200, 255, cv2.THRESH_BINARY)
    return bin_B|bin_G|bin_R
cv2.imshow("bin", bin(I))
cv2.waitKey()
