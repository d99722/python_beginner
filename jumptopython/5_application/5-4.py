# -*- coding:utf-8 -*-
# class Bird:
#     def fly(self):
#         raise NotImplementedError
#
# class Eagle(Bird):
#     def fly(self):
#         print("very fast")
#
# eagle = Eagle()
# eagle.fly()

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
