import sys

option = sys.argv[1]

if option == "-a":
    memo = sys.argv[2]
    f = open("test2.txt", 'a')
    f.write(memo)
    f.write('\n')
    f.close()

elif option == "-v":
    f = open("test.txt")
    memo = f.read()
    f.close()
    print(memo)
