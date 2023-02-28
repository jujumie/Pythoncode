#Create a program called countVowels.py that has a function that takes in an argument and prints the number of vowels
# in the string.  It should work for both lowercase and uppercase vowels.

import sys

x = sys.argv[1]

def countV():
    vowels = 'aeiouAEIOU'
    count = 0
    word = x
    for i in word:
        if i in vowels:
            count += 1
    print(count)

countV()