x = {12, 45}

print(x, id(x))

y = x.copy()

print(y, id(y))

print(x is y)
print(x is not  y)