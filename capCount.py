#Create a program called capCount.py that has a function that takes in a string and prints the number of capital
# letters in it.

import sys

x = sys.argv[1]

def capcount():
    print(sum(1 for letter in x if letter.isupper()))

capcount()