# global level variable
x = 78

class A:
    x = 2

    def __init__(self):
        self.x = 34
        print(x)       

a = A()


