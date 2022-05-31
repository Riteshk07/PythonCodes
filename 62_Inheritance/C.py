# Multilevel Inheritance 
class A:
    def pro1(self):
        print("Aur bhai kesa hai")
    
class B(A):
    def pro2(self):
        print("Sab badiya")
    
#class C(A,B):
#    pass
    
class C(B):
    pass

x= C()

x.pro1()
x.pro2()