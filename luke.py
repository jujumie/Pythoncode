#Create a program, luke.py, using the following dictionary:

import sys

relations = {'Darth Vader': 'father', 'Leia': 'sister', 'Han': 'brother in law', 'R2D2': 'droid', 'Rey': 'Padawan',
             'Tatooine': 'homeworld'}

x = sys.argv[1]

def luke():
    if x == 'Darth Vader':
        print('No, I am your father')

    else:
        print(f'Luke, I am your {relations[x]}')

luke()
