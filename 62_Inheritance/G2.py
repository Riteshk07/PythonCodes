# Method Resolution Order (mro)

class A:
    pass

class B(A):
    pass


print(B.mro())
print(A.mro())

print(ZeroDivisionError.mro())