#Create a program, mintosec.py, that takes one integer argument representing a number of minutes.
# The program will convert the argument to the corresponding number of seconds, and print that value out.

import sys

x = int(sys.argv[1])

mintosec = x * 60

print(round(mintosec, 2))