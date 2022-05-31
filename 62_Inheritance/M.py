class D:
    pass

class C:
    pass

class A(D):
    pass

class B(C):
    pass

class X(A, B, C):
    pass

print(X.mro())