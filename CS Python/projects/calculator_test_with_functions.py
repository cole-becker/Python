import math
from pcinput import getInteger

def getAddition():
    result = (x + y)
    print(x, "+", y, "is: ", result)

def getSubtraction():
    result = (x - y)
    print(x, "-", y, "is: ", result)

def getMultiply():
    result = (x * y)
    print(x, "times", y, "is: ", result)

def getDivision():
    result = (x / y)
    print(x, "divided by", y, "is: ", result)


while True:
    data = input("Hello! Would you like the (a)dd, (s)ubtract, (m)ultiply, (d)ivide or (e)xit: ").lower()
    if data == 'e':
        break
    if data in ('a', 's', 'm', 'd'):
        x = getInteger("please enter number 1 (0 to exit): ")
        if x == 0:
            break
        y = getInteger("please enter number 2 (0 to exit): ")
        if y == 0:
            break

        if data == 'a':
            getAddition()
                
        elif data == 's':
            getSubtraction()
                
        elif data == 'm':
            getMultiply()
            
        elif data == 'd':
            getDivision()
            
    else:
        print("that is not a valid response.")

print("Goodbye!")
                                             