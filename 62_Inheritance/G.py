class A:
    def pro(self):
        print('pro in A')

class B(A):
    def pro(self):
        print('pro in B')

x = B()

x.pro()