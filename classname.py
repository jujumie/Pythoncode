import sys

x = sys.argv[1]

class person():
    def __init__(self):
        pass

    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'My name is {self.name} and I am a {self.__class__.__name__}')


code = person(x)

code.hello()
print(code.__class__)

