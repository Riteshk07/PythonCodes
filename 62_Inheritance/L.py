class F:
    pass

class D(F):
    pass

class E(F):
    pass

class A(D):
    pass

class B(D, E):
    pass

class C(E):
    pass

class X(A, B, C):
    pass


print(X.mro())