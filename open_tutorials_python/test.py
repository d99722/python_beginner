# -*- coding=utf-8 -*-
class Cal(object):
    _history = []
    count = 0
    def __init__(self,v1,v2):
        if isinstance(v1,int):
            self.v1=v1
        if isinstance(v2,int):
            self.v2=v2
    def add(self):
        Cal.count = Cal.count + 1
        result = self.v1+self.v2
        Cal._history.append("add : %d + %d = %d" % (self.v1, self.v2, result))
        return result
    def subtract(self):
        Cal.count = Cal.count + 1
        result = self.v1-self.v2
        Cal._history.append("subtract : %d - %d = %d" % (self.v1, self.v2, result))
        return result
    def setV1(self,v):
        if isinstance(v,int):
            self.v1=v
    def setV2(self,v):
        if isinstance(v,int):
            self.v2=v
    def getV1(self):
        return self.v1
    def getV2(self):
        return self.v2

    @classmethod
    def history(cls):
        th = 0
        for item in Cal._history:
            th = th + 1
            print('%d.'%(th) +item)

    @classmethod
    def getCount(cls):
        print('총 %d회 계산. 실행 종료'%(Cal.count))

class CalMultiply(Cal):
    def multiply(self):
        Cal.count = Cal.count + 1
        result = self.v1*self.v2
        Cal._history.append("multiply : %d * %d = %d" % (self.v1, self.v2, result))
        return result

class CalDivide(CalMultiply):
    def divide(self):
        Cal.count = Cal.count + 1
        result = self.v1/self.v2
        Cal._history.append("divide : %d / %d = %d" % (self.v1, self.v2, result))
        return result

c1=CalMultiply(10,20)
c1.add()
c1.multiply()

c2=CalDivide(20,10)
c2.add()
c2.subtract()
c2.multiply()
c2.divide()

c3=CalDivide(840,5)
c3.add()
c3.subtract()
c3.multiply()
c3.divide()

print(c3.getV1())
c3.setV1(10)
print(c3.getV1())
c3.add()
c3.subtract()
c3.multiply()
c3.divide()

Cal.history()
Cal.getCount()
