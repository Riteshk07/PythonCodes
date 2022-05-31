class A:
    def pro(self):
        print("parant A")

class B(A):
    def info (self):
        print("+++++++")
        self.pro()

x = B()
x.info()