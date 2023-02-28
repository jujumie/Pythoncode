#Create a program, username.py, that has a function that takes as arguments a first and last name and creates a
# username.  The username will be the first letter of the first name in lowercase, the last 7 of the last name in
# lowercase, and the total number of characters in the first and last names.  For example, Eastern University would
# be eversity17.
#The program should print "Your username is x" where x is the username.

import sys

first_name = sys.argv[1]
last_name = sys.argv[2]
first_letter = first_name[0].lower()
last_7 = last_name[-7:].lower()
user = first_letter + last_7

def username():
    print(f'Your username is {user + str(len(first_name + last_name))}')

username()