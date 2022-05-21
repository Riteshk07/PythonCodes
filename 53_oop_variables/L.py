x = 39

class A:
    def __init__(self):
        self.x = 99
        print(A.x)       

a = A()

# AttributeError: type object 'A' has no attribute 'x'
