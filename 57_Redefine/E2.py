class A :
    @staticmethod
    def pro():
        print("Ritesh the Grate")

class B(A):
    @classmethod
    def pro(cls):
        print("Ritesh is a good boy")
 
A.pro()
B.pro()