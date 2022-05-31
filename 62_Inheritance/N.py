class H:
    pass

class F(H):
    pass

class G(H):
    pass

class C(F):
    pass

class D(F, G):
    pass

class E(G):
    pass

class A(C, D):
    pass

class B(D, E):
    pass

class X(A, B):
    pass


print(X.mro())