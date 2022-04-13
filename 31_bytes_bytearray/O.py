x = [23, 12, 9] 

# y = bytearray(x)
#vs
y = bytes(x)  # TypeError: 'bytes' object does not support item assignment

y[1] = 99

print(y[0])
print(y[1])
print(y[2])