#Q10
class Calculator:
    def __init__(self,numberList):
        self.numberList = numberList

    def sum(self):
        result = 0
        for num in self.numberList:
            result += num
        print(result)

    def avg(self):
        result = 0
        for num in self.numberList:
            result += num
        print(result/len(self.numberList))

cal1 = Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()

cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()
