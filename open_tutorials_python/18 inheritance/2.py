class Cal(object):
    def __init__(self,v1,v2):
        if isinstance(v1,int):
            self.v1 = v1
        if isinstance(v2,int):
            self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    def setV1(self,v):
        if isinstance(v,int):
            self.v1 = v
    def getV1(self):
        return self.v1
    def setV2(self,v):
        if isinstance(v,int):
            self.v2 = v
    def getV2(self):
        return self.v2

class CalMultiply(Cal):
    def multiply(self):
        return self.v1*self.v2

class CalDivide(CalMultiply):
    def divide(self):
        return self.v1/self.v2

c1=CalMultiply(10,10)
print(c1.add())
print(c1.subtract())
print(c1.multiply())
# c1.setV1(30)
# c1.setV2(20)
# print(c1.getV1(),c1.getV2())
# print(c1.add())
# print(c1.subtract())
# print(c1.multiply())

c2=CalDivide(20,10)
print(c2, c2.add())
print(c2, c2.subtract())
print(c2, c2.multiply())
print(c2, c2.divide())
