class A :
    def __init__(self, x):
        self.x = x
class B(A):
    def __init__(self, y):
        self.y = y
class C(B):
    def __init__(self, z):
        self.z = z

t = C(45)

# print(t.x)
# print(t.y)
print(t.z)