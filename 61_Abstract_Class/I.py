class A:
    def pro(self):
        print("Pro in A")
    
class B:
    def pro(self):
        print("Pro in B")
    
#class C(A,B):
#    pass
    
class C(B,A):
    pass
x= C()

x.pro()