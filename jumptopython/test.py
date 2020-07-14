import re
import sys

def game369(real):

    say = input("Enter the next number : ")
    match = re.search(r'3|6|9', str(real))

    if match == None:
        if str(real) == (say):
            game369(real+1)
        else:
            over()
    else:
        if say == "clap":
            game369(real+1)
        else :
            over()

def over():
    print("Game Over ! ")
    sys.exit()

real = 1
game369(real)
