import sys
import numpy as np

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

def reallyrandom():
    np.random.seed(42)
    if z < x:
        array = np.random.randint(0, 10, size= x, dtype=int) * y
        index_1 = array[z]
        print(f'Your random value is {index_1}')

    else:
        return

reallyrandom()