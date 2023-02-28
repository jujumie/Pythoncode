#Create a program inrange.py that has a function that takes one integer argument.  The function will print a list of
# all values between 5000 and 8000 that is divisible by (1) the integer argument, and (2) the argument + 4.

import sys

x = int(sys.argv[1])

def numrange():
    numbers = []
    for i in range(5000, 8000):
        if (i % x == 0) and i % (x + 4) == 0:
            numbers.append(i)

    print(numbers)

numrange()