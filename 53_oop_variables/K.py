x = 39

class A:
    def __init__(self):
        print(A.x)       

a = A()

# AttributeError: type object 'A' has no attribute 'x'
