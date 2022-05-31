class A:
    @staticmethod
    def pro():
        print("Parent A")

class B (A):
    @staticmethod 
    def info():
        print ("+++++")
        super().pro()

B.info()

# RuntimeError: super(): no arguments