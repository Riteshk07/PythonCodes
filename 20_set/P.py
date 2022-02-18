x = {1,2,3}

# y = 99         # TypeError: 'int' object is not iterable
# y = {33,22}
# y = [11,22]
# y = (44,55)

print(x, id(x))

x.update(y)

print(x, id(x))