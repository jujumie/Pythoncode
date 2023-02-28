#Create a program, quadratic.py, that takes in three arguments that represent
#the a, b, and c values in the quadratic formula.  The values should be to two
#decimal places.  You do not need to account for imaginary values.  Then print
#out both roots in the form:

#The solutions are x and y

#Where x and y correspond to the positive and negative roots, respectively.

import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

def quad():
    x = (b ** 2) - (4 * a * c)

    if x > 0:
        x1 = round((- b + math.sqrt(x)) / (2*a),2)
        x2 = round((- b - math.sqrt(x)) / (2*a),2)
        print(f'The solutions are {x1} and {x2}')

    else:
        print('not applicable. try again')

quad()
