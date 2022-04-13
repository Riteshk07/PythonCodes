# x = [12, 45, 255, 256]    #NOT OK
# x = [12, 45, 255, 0]
x = [12, 45, 255, -1]   #NOT OK

y = bytes(x)

print(y[0])
print(y[1])
print(y[2])
print(y[3])


# ValueError: bytes must be in range(0, 256)