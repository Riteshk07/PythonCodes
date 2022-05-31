class A :
    x= 20

class B(A):
    @classmethod
    def pro(cls):
        print(x)

B.pro()