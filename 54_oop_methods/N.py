class A:
    def __str__(self):
        return "rajmohan"
        
class B (A):
    pass
    
x = A()
y = B()
print(x.__str__())
print(y)
print(y.__str__())