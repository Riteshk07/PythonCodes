class E:
    pass

class F:
    pass

class B(E):
    pass

class C(E, F):
    pass

class D(F):
    pass

class A(B, C, D):
    pass

print(A.mro())