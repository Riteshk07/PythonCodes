class A:
    def pro(self):
        print("parant A")

class B(A):
    def pro(self):
        print("Child B")
    def info (self):
        print("+++++++")
        self.pro()
        super().pro()

x = B()
x.info()