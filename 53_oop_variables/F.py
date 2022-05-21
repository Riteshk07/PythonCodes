class A:
    x = 9

    def __init__(self):
        # x = 43
        self.x = 56
        print(x)       # NameError: name 'x' is not defined
        print(self.x)
        print(A.x)    

a = A()


