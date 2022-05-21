class A:
    x = 9

    def __init__(self):
        self.x = 56
        print(self.x)

a = A()

print(A.__dict__)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(a.__dict__)