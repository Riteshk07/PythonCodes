x = [89, 56, 78, 34, 9, 23, 1,  12]

print(x)

# Case 1:
# s = x.pop(1)     # here 1 is treated as an index 
# print(s)         # because the value being removed is not known that is why will be returned

#Case 2:
t = x.remove(1)  # here 1 will be treated as a value
print(t)         # because the eargument is treated as a value and we know what is being removed thus the method does not return the value, instead returns None.

print(x)