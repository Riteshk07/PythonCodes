x = {1,2,3}
y = {4,5}

print(x, id(x))

# x.extend(y)   # AttributeError: 'set' object has no attribute 'extend'

x.update(y)

print(x, id(x))