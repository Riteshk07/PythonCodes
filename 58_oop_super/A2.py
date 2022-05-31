class A :
    x= 20

class B(A):
    x= 45
    @classmethod
    def pro(cls):
        print(cls.x)
        print(super().x)

B.pro()