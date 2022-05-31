# poly(many) morphism(forms)
class A :
    def pro(self):
        print("Hello ji")

class B(A):
    # method overriding
    def pro(self):
        print("Bye ji")
x = A()
y = B()

x.pro()
y.pro()