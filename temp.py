#Create a program, temp.py, that takes in one numeric argument representing a Celsius value.  Then, print out the
# corresponding Fahrenheit value to two decimals in the form:
#The temperature is x degrees Fahrenheit.
#Where x is the calculated Fahrenheit value

import sys

x = float(sys.argv[1])
temp_convert = '{:.2f}'.format(round((x * (9.00/5.00) + 32.00) ,2))

def temp():
    print(f'The temperature is {temp_convert} degrees Fahrenheit.')

temp()