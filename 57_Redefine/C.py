class A :
    def pro(self):
        print("Hello ji")

class B(A):
    pass
x = A()
y = B()

x.pro()
y.pro()