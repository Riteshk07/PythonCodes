class A :
    def __init__(self, x):
        self.x = x
class B(A):
    pass 
t = B(56)

print(t.x)