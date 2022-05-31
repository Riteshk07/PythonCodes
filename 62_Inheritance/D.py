# Hierarchical Inheritance

class A:
    x = 111

class B(A):
    pass

class C(A):
    pass

print(B.x, C.x)