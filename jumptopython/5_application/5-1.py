# -*- coding: utf-8 -*-

# class Calculator:
#     def __init__(self):
#         self.result=0
#
#     def add(self, num):
#         self.result += num
#         return self.result
#
#     def sub(self,num):
#         self.result -= num
#         return self.result
#
# cal1 = Calculator()
# cal2 = Calculator()
#
# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

# class Cookie:
#     pass
#
# a = Cookie()
# b = Cookie()
#
# class FourCal:
#     def __init__(self,first,second):
#         self.first = first
#         self.second = second
#
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#
#     def add(self):
#         result = self.first + self.second
#         return result
#
#     def sub(self):
#         result = self.first - self.second
#         return result
#
#     def mul(self):
#         result = self.first * self.second
#         return result
#
#     def div(self):
#         result = self.first / self.second
#         return result
#
# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result
#
# class SafeFourCal(FourCal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else :
#             return self.first / self.second
#
# class FailFourCal(FourCal):
#     def mul(self):
#         if self.first == 0 or self.second == 0:
#             return "fail"
#         else:
#             return self.first * self.second
#
# a = FourCal(4,2)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())
# a.setdata(6,3)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())

# b = MoreFourCal(4,2)
# print(b.pow())
#
# c = FailFourCal(0,0)
# print(c.mul())


class Family:
    lastname = "김"

print(Family.lastname)

a=Family()
b=Family()
print(a.lastname)
print(b.lastname)

Family.lastname = "이"
print(a.lastname)
print(b.lastname)
