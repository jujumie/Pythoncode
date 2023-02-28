import sys

x = sys.argv[1]

def phrase():
    long = max(x.split(' '), key=len)

    print(f'The longest word is {long.lower()}')

phrase()