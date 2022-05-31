class A:
    @classmethod
    def pro(cls):
        print("Hello")

class B(A):
    pass 
B.pro()