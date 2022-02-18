# x,y,z = 1,2,3,4   # ValueError: too many values to unpack (expected 3)
x,y,z = 1,2         # ValueError: not enough values to unpack (expected 3, got 2)

print(x, y, z)