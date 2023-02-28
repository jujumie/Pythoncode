#Create a program, gpacalc.py, that takes four letter grade arguments and prints out the corresponding GPA, to two
# decimals. Your program should work both in arguments are upper-case and lower-case.  Your program should print in
# the form:

#My GPA is x

import sys

w = sys.argv[1].upper()
x = sys.argv[2].upper()
y = sys.argv[3].upper()
z = sys.argv[4].upper()

def gpacalc():
    grades = {'A': 4.0, 'A-': 3.66, 'B+': 3.33, 'B': 3.0, 'B-': 2.66, 'C+': 2.33, 'C': 2.0, 'C-': 1.66, 'D+': 1.33,
           'D': 1.00, 'D-': .66,
           'F': 0.00}
    total = round((grades[w] + grades[x] + grades[y] + grades[z]) / 4, 2)
    print(f'My GPA is {total}')

gpacalc()