class A:
    def pro1(self):
        print("Pro1 in A")
    
class B:
    def pro2(self):
        print("Pro2 in B")
    
class C(A,B):
    pass
    
x= C()

x.pro1()
x.pro2()