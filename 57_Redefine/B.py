class A :
    x=90
class B(A):
    # redefinne the variable x 
    x= 321
print(B.x)
print(A.x)
