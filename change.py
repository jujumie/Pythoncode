#Create a program, change.py, that has a function that takes 4 arguments that correspond to the number of quarters,
# dimes, nickels, and pennies, respectively.  Calculate the total value of that change, and print "The total value of
# your change is $x" where x is equal to the total value.

import sys

x = round(.25*int(sys.argv[1]) + .1*int(sys.argv[2]) + .05*int(sys.argv[3]) + .01*int(sys.argv[4]),2)

def change():
    print(f'The total value of your change is ${x}')

change()