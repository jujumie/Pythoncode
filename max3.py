#Create a program, max3.py, that has a function that takes three integer arguments.  The program will then print out
# the highest of the three values.

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

def maximum():
    print(max(x, y, z))

maximum()