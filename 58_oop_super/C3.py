class A :
    @classmethod 
    def pro(cls):
        print("Parent A")

class B(A):
    @classmethod 
    def pro2(cls):
        print("Parent B")

    @classmethod 
    def info(cls):
        print("++++++")
        cls.pro2()
        cls.pro()

B.info()