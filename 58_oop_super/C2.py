class A:
    @classmethod
    def pro(cls):
        print("Parent A ")

class B(A):
    @classmethod 
    def pro(cls):
        print("Child B")
    @classmethod 
    def info(cls):
        print("+++++")
        cls.pro()
        super().pro()

B.info()