#Create a program, digits.py, that has a function that takes a number and prints the number of digits in the number.
# It should work for numbers with decimals, too.

import sys


def numberz():
    x = sys.argv[1]
    y = x.replace('.', '')
    print(len(y))

numberz()