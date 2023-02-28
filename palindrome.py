#Create a program, palindrome.py, that has a function that takes one string argument and prints a sentence indicating
# if the text is a palindrome.  The function should consider only the alphanumeric characters in the string, and not
# depend on capitalization, punctuation, or whitespace.

import sys

x = sys.argv[1]

def palindrome():
    y = ""
    for i in x:
        if i.isalnum():
            y += i.lower()

    for i in range(0, int(len(y) / 2)):
        if y[i] != y[len(y) - i - 1]:
            return False

        else:
            return True

if palindrome():
    print("It's a palindrome!")

else:
    print("It's not a palindrome!")

palindrome()
