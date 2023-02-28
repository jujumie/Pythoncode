#Create a program called randdf.py that has a function that takes two integer arguments and prints a Pandas
# dataframe.  The two arguments will correspond to the number of rows and number of columns, respectively.
# The dataframe should be filled with random integers from 0 to 100.  Set your random seed to 56.

import sys
import numpy as np
import pandas as pd

x = int(sys.argv[1])
y = int(sys.argv[2])

def randomdf():
    np.random.seed(56)
    randdf = pd.DataFrame(np.random.randint(0, 100, size=(x, y)))
    print(randdf)

randomdf()
