# -*- coding: utf-8 -*-

# def add(a,b):
#     return a+b
#
# c=add(2,3)
# print(c)

# def add(a,b):
#     result = a+b
#     return result
#
# a = add(3,4)
# print(a)

# def say():
#     return 'Hi'
#
# a = say()
# print(a)

# def add(a,b):
#     print("%d, %d의 합은 %d 입니다." % (a, b, a+b))
#
# add(3,4)

# def say():
#     print("Hi!")
#
# say()

# def add(a,b):
#     return a+b
#
# result = add(a=3, b=7)
# print(result)

# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result
#
# result = add_many(1,5,2)
# print(result)

# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result += i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result *= i
#     return result
#
# a1 = add_mul("add", 1, 5, 2)
# a2 = add_mul("mul", 1, 5, 2)
# print(a1)
# print(a2)

# def add_and_mul(a,b):
#     return a+b, a*b
# result1, result2 = add_and_mul(3,4)
# print(result1)

# def add_and_mul(a,b):
#     return a+b
#     return a*b

# def say_nick(nick):
#     if nick == "바보":
#         return
#     print("나의 별명은 %s입니다." % nick)
#
# say_nick("천재")
# say_nick("바보")
# say_nick("곤짱")

# def say_myself(name, old, man=True):
#     print("나의 이름은 %s입니다." % name)
#     print("나이는 %d살입니다." % old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")
#
# say_myself('박응용', 27, True)

# a = 1
# def vartest(a):
#     a = a + 1
#
# vartest(a)
# print(a)

# def vartest(a):
#     a= a+1
# vartest(3)
# print(a)

# a = 1
# def vartest(a):
#     a = a + 1
#     return a
#
# a = vartest(a)
# print(a)
#
# a = 1
# def vartest():
#     global a
#     a = a + 1
#
# vartest()
# print(a)

def add(a,b):
    return a+b

result = add(3,4)
print(result)
