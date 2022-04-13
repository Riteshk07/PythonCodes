x = [23, 12, 9] 

# y = bytearray(x)
#vs
y = bytes(x)  

y.add(99)    #AttributeError: 'bytes' object has no attribute 'add'
y.append(99) #AttributeError: 'bytes' object has no attribute append

print(y[0])
print(y[1])
print(y[2])
print(y[3])