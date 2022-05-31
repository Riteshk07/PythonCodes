class D:
    pass

class C:
    pass

class B:
    pass

class A(B, C, D):
    pass

print(A.mro())