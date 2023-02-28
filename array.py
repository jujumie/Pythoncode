#Create a program called array.py that has a function that takes four integer arguments.  Those arguments should be put
# into an Numpy array.  The function will have two print statements.  The first will print the type of the array you
# create (which should be <class ‘numpy.ndarray’>).  The second will print the sum of the four items in your array.
#Your output could look like this (it could differ in parts):

	#<class ‘numpy.ndarray’>
	#14

import sys
import numpy as np

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])

array_1 = np.array([a, b, c, d])


def number_array():
    print(type(array_1))
    print(np.sum(array_1))


number_array()