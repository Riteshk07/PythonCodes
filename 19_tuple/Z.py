# x = [1,2,5]
x = (1,2,5)

y = x.copy()    # AttributeError: 'tuple' object has no attribute 'copy'

print(x, id(x))
print(y, id(y))