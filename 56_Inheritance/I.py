class A :
    w=89
class B(A):
    r=90
class C(B):
    t=45

print(C.t, C.r, C.w)