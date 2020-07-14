# -*- coding=utf-8 -*-

# 두 수를 입력받기
# 1, 2
# 연산 타입 입력받기
# subtract
# 결과 : n번째 연산, 1 - 2 = -1
#
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
        Cal._history.append("%d + %d = %d" % (self.v1, self.v2, result))
        return result
    def subtract(self):
        Cal.count = Cal.count + 1
        result = self.v1-self.v2
        Cal._history.append("%d - %d = %d" % (self.v1, self.v2, result))
        return result
    def multiply(self):
        Cal.count = Cal.count + 1
        result = self.v1*self.v2
        Cal._history.append("%d * %d = %d" % (self.v1, self.v2, result))
        return result
    def divide(self):
        Cal.count = Cal.count + 1
        result = self.v1/self.v2
        Cal._history.append("%d / %d = %d" % (self.v1, self.v2, result))
        return result
    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)

    @classmethod
    def getCount(cls):
        print('%d번째 계산'%(Cal.count))


exit_checker = '1'
cal_checker = ['add', 'sub', 'mul', 'div']

while exit_checker == '1' :
    print('두 수를 입력하시오')
    v1, v2 = input().split()
    v1 = int(v1)
    v2 = int(v2)
    ccl = input('원하는 연산을 입력하시오\nadd, sub, mul, div\n')

    for item in cal_checker:
        if item == ccl:
            u_input = Cal(v1,v2)
            print(type(item))
            u_input.add()
            u_input.getCount()
            u_input.history()
        else :
            print('재')
    #
    # if ccl=='add':
    #     u_input = Cal(v1,v2)
    #     u_input.add()
    #     u_input.getCount()
    #     u_input.history()
    # elif ccl=='subtract':
    #     u_input = Cal(v1,v2)
    #     u_input.subtract()
    #     u_input.getCount()
    #     u_input.history()
    # elif ccl=='multiply':
    #     u_input = Cal(v1,v2)
    #     u_input.multiply()
    #     u_input.getCount()
    #     u_input.history()
    # elif ccl=='divide':
    #     u_input = Cal(v1,v2)
    #     u_input.divide()
    #     u_input.getCount()
    #     u_input.history()
    # else:
    #     print('잘못입력하셨습니다.\n')

    exit_checker = input('계속 이용하시겠습니까?\nyes = 1, no=*\n')
print('실행 종료')
