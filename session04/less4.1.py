# class Ten_class:
#thuoc tinh : variable
#phuown thuc :hàm con

class Hcn:
    width = 10
    height = 100
    def __init__(self,w,h):
        self.width = w
        self.height = h
    def chuvi(self):
        c = (self.height + self.width)*2
        return c

# tạo
a1 = Hcn(10,100)
a2 = Hcn(30,100)
cv = a1.chuvi()
cv2 = a2.chuvi()
print (cv)
print(cv2)