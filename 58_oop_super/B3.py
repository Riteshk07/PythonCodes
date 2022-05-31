class A:
    def pro(self):
        print("parant A")

class B(A):
    def pro2(self):
        print("Child B")
    def info (self):
        print("+++++++")
        self.pro()
        self.pro2()

x = B()
x.info()