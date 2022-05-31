class A:
    pass
# print(A.__hash__())
# print(A.__str__())
# print(A.__init__()) 
# TypeError: descriptor '__init__' of 'object' object needs an argument
print(A)

x = A()
print(x.__hash__())
print(hex(x.__hash__()))
print(x.__str__())
print(x)
