class A:
    def __init__(self, value):
        self.value= value
        
    def __str__(self):
        return str(self.value)
        
    def __lt__(self, val):
        print(f"{self.value} is less than {val.value}",end=" : ")
        return self.value < val.value
        
    def __le__(self, val):
        print(f"{self.value} is less than equal to {val.value}",end=" : ")
        return self.value <= val.value
        
    def __gt__(self, val):
        print(f"{self.value} is grater than {val.value}",end=" : ")
        return self.value > val.value
        
    def __ge__(self, val):
        print(f"{self.value} is grater than Equal {val.value}",end=" : ")
        return self.value >= val.value
        
    def __eq__(self, val):
        print(f"{self.value} is Equal to {val.value}",end=" : ")
        return self.value == val.value
        
    def __ne__(self, val):
        print(f"{self.value} is not Equal {val.value}",end=" : ")
        return self.value != val.value  
        
    def __add__(self, val):
        print(f"Addition of {self.value} and {val.value}",end=" : ")
        return self.value + val.value 
        
    def __mul__(self, val):
        print(f"Multiply of {self.value} and {val.value}",end=" : ")
        return self.value * val.value 
        
    def __sub__(self, val):
        print(f"Subtraction of {self.value} and {val.value}",end=" : ")
        return self.value - val.value 
        
    def __mod__(self, val):
        print(f"Modulus of {self.value} and {val.value}",end=" : ")
        return self.value % val.value 
        
    def __truediv__(self, val):
        print(f"Division of {self.value} and {val.value}",end=" : ")
        return self.value / val.value
        
    def __pow__(self, val):
        print(f"{self.value} Power of {val.value}",end=" : ")
        return self.value ** val.value
        
    def __concat__(self, val):
        print(f"Concatination of {self.value} and {val.value}",end=" : ")
        return self.value + val.value
        
    def is_(self, val):
        print(f"{self.value} is {val.value}",end=" : ")
        return self.value is val.value
        
    def is_not(self, val):
        print(f"{self.value} is not {val.value}",end=" : ")
        return self.value is not val.value  
        
# Addition
x1 = A(15)
y1 = A(45)
print(x1+y1)
 
# subtraction
x = A(15)
y = A(45)
print(x-y)
 
# Multi
x2 = A(15)
y2 = A(3)
print(x2*y2)
 
 # Division
x3 = A(60)
y3 = A(3)
print(x3/y3)
 
 # Mod
x4 = A(18)
y4 = A(7)
print(x4%y4)
 
 # less
x5 = A(16)
y5 = A(89)
print(x5<y5)
 
 # Equal
x6 = A(56)
y6 = A(56)
print(x6==y6)
 
 # not Equal
x7 = A(60)
y7 = A(3)
print(x7!=y7)
 
 # less Equal
x8 = A(56)
y8 = A(98)
print(x8<=y8)
 
 # grater Equal
x9 = A(60)
y9 = A(60)
print(x9>=y9)
 
 # Power
x11 = A(2)
y11 = A(3)
print(x11**y11)
 
 # is 
x12 = A("Ritesh")
y12 = A("Ritesh")
print(x12 is y12)
 
 # is not
x13 = A("Ritesh")
y13 = A("Rajkumar")
print(x13 is not y13)
 
 # Concat
x14 = A("Ritesh")
y14 = A(" koshta")
print(x14.__concat__(y14))
 
 