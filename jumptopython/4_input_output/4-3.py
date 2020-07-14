# -*- coding: utf-8 -*-

# f = open("새파일.txt", 'w')
# f.close()

# f = open("새파일.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# for i in range(1,11):
#     data = "%d번째 줄입니다.\n" % i
#     print(data)

# f = open("새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()

# while 1:
#     data = input()
#     if not data:
#         break
#     print(data)

# f=open("새파일.txt",'r')
# data = f.read()
# print(data)
# f.close()

# f=open("새파일.txt", 'a')
# for i in range(11,20):
#     data = "%d번째 줄입니다.\n"% i
#     f.write(data)
# f.close()

# with open("새파일.txt", "w") as f:
#     f.write("Life is too short, you need python")

# import sys
#
# args = sys.argv[0:]
# for i in args:
#     print(i)

import sys
args = sys.argv[:]
for i in args:
    print(i.upper(), end=' ')
