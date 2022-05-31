# Multiple Inheritance 
class A:
    def pro(self):
        print("Aur bhai kesa hai")
    
class B:
    def pro(self):
        print("Sab badiya")
    
#class C(A,B):
#    pass
    
class C(B,A):
    pass
x= C()

x.pro()