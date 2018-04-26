class Hcn:
    def __init__(self,w,h):
        self.width = w
        self.height = h
    def dientich(self):
        s = self.width * self.height
        return s
a = Hcn(10,20)
print(a.dientich())