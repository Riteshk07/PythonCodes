class A:
    x = 9

    def __init__(self):
        x = 43
        self.x = 56
        # print(x)
        # print(self.x)
        # print(A.x)
        print(locals())

a = A()

print(a.__dict__)
print(A.__dict__)

