class A :
    def __init__(self, x):
        self.x = x
class B(A):
    pass

t = A(54)
s = B(23)

print(t.x, s.x)

s.x = 99

print(t.x, s.x)