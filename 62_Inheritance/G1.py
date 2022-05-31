class A:
    def pro(self):
        print('pro in A')

class B(A):
    pass

x = B()

x.pro()