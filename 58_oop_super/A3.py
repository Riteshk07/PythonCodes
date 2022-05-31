class A :
    x= 20

class B(A):
    y= 46
    @classmethod
    def pro(cls):
        print(cls.x)
        print(cls.y)

B.pro()