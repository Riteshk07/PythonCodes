class A:
    @classmethod
    def pro(cls):
        print("Hello")

class B(A):
    @classmethod
    def pro(cls):
        print("Hiiiiiii")

A.pro()
B.pro()